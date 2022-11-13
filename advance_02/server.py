import argparse
import queue
import socket
import struct
import threading
from threading import Thread
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Server:
    def __init__(self, k=10, workers_num=5):
        self.conn = None
        self.socket = socket.socket()
        self.socket.bind(("localhost", 5001))
        self.socket.settimeout(10)
        self.k = k
        self.workers_num = workers_num
        self.queue = queue.Queue()
        self.sem = threading.Semaphore(1)
        self.threads = [Thread(target=self.cnt_freq, args=(self.queue, self.sem)) for _ in range(self.workers_num)]
        self.url_num = 0

    def run(self):
        try:
            self.socket.listen()
            while True:
                conn, addr = self.socket.accept()
                self.conn = conn
                with conn:
                    for th in self.threads:
                        th.start()
                    cur_url = self.recv_msg(conn)
                    while cur_url:
                        cur_url = cur_url.decode('unicode_escape')
                        self.queue.put(cur_url)
                        cur_url = self.recv_msg(conn)
                self.conn = None
                self.queue.put(None)
                for th in self.threads:
                    th.join()
        except socket.timeout:
            self.socket.close()

    def cnt_freq(self, que, sem):
        while True:
            try:
                url = que.get()
            except queue.Empty:
                continue

            if url is None:
                que.put(None)
                break

            data = urlopen(url).read()
            soup = BeautifulSoup(data)
            data = soup.get_text()
            words = data.split()
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
            top_k_words = {word: freq for word, freq in word_freq[:self.k]}
            msg = (url + " " + str(top_k_words)).encode('unicode_escape')

            with sem:
                if self.conn:
                    msg = struct.pack('>L', len(msg)) + msg
                    self.conn.send(msg)
                else:
                    print("Connection was closed")
                    break
            self.url_num += 1
            print(f"Processed {self.url_num}")

    def send_msg(self, sock, msg):
        if sock:
            msg = struct.pack('>L', len(msg)) + msg
            sock.send(msg)
        else:
            print("Connection was closed")

    def recv_msg(self, sock):
        if sock:
            raw_msglen = sock.recv(4)
            if not raw_msglen:
                return None
            msglen = struct.unpack('>L', raw_msglen)[0]
            msg = sock.recv(msglen)
            return msg
        else:
            print("Connection was closed")


parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workers', type=int, default=10)
parser.add_argument('-k', '--keys_num', type=int, default=10)


if __name__ == "__main__":
    args = parser.parse_args()
    s = Server(k=args.keys_num, workers_num=args.workers)
    s.run()
