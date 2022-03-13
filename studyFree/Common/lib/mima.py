# -*- coding:utf-8 -*-
# @FileName  :mima.py
# @Time      :2022/3/11 12:42
# @Author    :JN


import random
import string

import time


def time_salt():
    unix_time = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime()), '%Y-%m-%d')))
    return str(unix_time)[0:8]


# 字符串加密
def encrypt(s):
    # 盐值用于加密钥生成
    salt_base = f"%@*{time_salt()[::-1]}*@%"

    n = int(len(s) / len(salt_base))
    # 加密钥
    salt = (n + 1) * salt_base
    encry_str = ''
    for i, j in zip(s, salt):
        ss = str(ord(i) + ord(j))
        cc = list(ss)
        for _ in range(5 - len(ss)):
            cc.insert(random.randint(0, len(cc) - 1), random.sample(string.ascii_letters, 1)[0])
        encry_str += ''.join(cc)

    return encry_str


def decipher(s):
    # 盐值用于加密钥生成
    salt_base = f"%@*{time_salt()[::-1]}*@%"
    p = ''
    n = int(len(s) / 5 / len(salt_base))
    # 加密钥
    salt = (n + 1) * salt_base
    s = [s[ii * 5: (ii + 1) * 5] for ii in range(0, int(len(s) / 5))]

    for i, j in zip(s, salt):
        ss = ''.join([ii for ii in i if ii.isdigit()])
        p += chr(int(ss) - ord(j))

    return p


if __name__ == "__main__":
    a = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    print(a)
    b = encrypt(a)
    print(b)
    c = decipher(b)
    print(c)
    print(a == c)
