""" 
ssppg - A simple and secure Python password generator. 
"""
# TODO: Look into cryptographically secure PRNG.

import platform
import string
import random
import sys

def generate_password(length, chars):
    password = ""
    for i in range(length):
        c = random.choice(chars)
        password += c

    return password
        
def main():
    shuffle_iterations = 100
    password_len = 50

    numbers = [str(i) for i in range(0,10)]
    all_chars = list(string.ascii_letters + string.punctuation) + numbers

    for i in range(shuffle_iterations):
        random.shuffle(all_chars)

    password = generate_password(password_len, all_chars)
    print(password)

if __name__ == '__main__':
    main()
