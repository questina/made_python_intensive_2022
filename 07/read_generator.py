"""
This module contains function
to read and filter lines from file
"""


def read_and_filter(fileobj, keywords):
    """
    This generator searches for keywords in contents of the file
    :param fileobj: input file
    :param keywords: keywords to search in lines of input file
    :return: file line with a keyword
    """
    cur_s = fileobj.readline()
    while cur_s != "":
        for keyword in keywords:
            if keyword.lower() in cur_s.lower().split():
                yield cur_s
                break
        cur_s = fileobj.readline()
