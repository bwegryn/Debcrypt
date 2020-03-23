#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from passlib.hash import bcrypt
from libs import pingo
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='A script crack bcrypt hash.')
parser.add_argument("--p", default="pass.txt", help="password file")
parser.add_argument("--h", default="hash.txt", help="hash file")

args = parser.parse_args()
password_file = args.p
hash_file = args.h
passwords = {}

text_file = open(password_file, "r")
hash_file = open(hash_file, "r")

words = text_file.read().splitlines()
hashes = hash_file.read().splitlines()

length = len(words)
print()

for (index, word) in enumerate(words):
    pingo(index, length, prefix='Wait:', suffix='Complete')
    if (len(passwords) == len(hashes)):
        break
    for hash in hashes:
        if (bcrypt.verify(word, hash)):
            passwords[hash] = word
            print()
            print("\nFound match: " + hash + ":" + word + "\n")
