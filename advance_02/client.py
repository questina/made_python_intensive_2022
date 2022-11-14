import argparse
import queue
import struct
import threading
from threading import Thread
import socket


class Client:
    def __init__(self, workers_num=5):
        self.workers_num = workers_num
        self.socket = socket.socket()
        self.queue = queue.Queue()
        self.sem = threading.Semaphore(1)
        self.threads = [Thread(target=self.send_url,
                               args=(self.queue, self.sem))
                        for _ in range(workers_num)]

    def connect(self, url_file):
        self.socket.connect(("localhost", 5001))
        with open(url_file, "r") as url_f:
            urls = url_f.readlines()
        for url in urls:
            self.queue.put(url.replace('\n', ''))
        self.queue.put(None)
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()
        self.socket.close()

    def send_url(self, que, sem):
        while True:
            try:
                url = que.get()
            except queue.Empty:
                continue

            if url is None:
                que.put(None)
                break

            with sem:
                self.send_msg(url.encode('unicode_escape'))
                data = self.recv_msg()
            if not data:
                break
            print(data.decode('unicode_escape'))

    def send_msg(self, msg):
        msg = struct.pack('>L', len(msg)) + msg
        self.socket.sendall(msg)

    def recv_msg(self):
        raw_msglen = self.socket.recv(4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>L', raw_msglen)[0]
        msg = self.socket.recv(msglen)
        return msg


parser = argparse.ArgumentParser()
parser.add_argument('threads_num', type=int)
parser.add_argument('url_filename', type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    c = Client(workers_num=args.threads_num)
    c.connect(url_file=args.url_filename)
