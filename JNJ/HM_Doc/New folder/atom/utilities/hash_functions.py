import hashlib
import os
import sys


def get_file_md5(filename: str, buf_size: int = 65536):
    if not os.path.exists(filename):
        raise FileNotFoundError(f'File {filename} not found to calculate MD5 hash.')
    with open(filename, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(buf_size)
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()


def get_file_sha1(filename: str, buf_size: int = 65536):
    if not os.path.exists(filename):
        raise FileNotFoundError(f'File {filename} not found to calculate MD5 hash.')
    with open(filename, 'rb') as f:
        sha1 = hashlib.sha1()
        while True:
            data = f.read(buf_size)
            if not data:
                break
            sha1.update(data)
        return sha1.hexdigest()
