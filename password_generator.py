""" 
ssppg - A simple and secure Python password generator. 
"""

import argparse
import platform
import string
import random
import sys

def generate_password(length, chars, shuffle_iterations):
    """
    Generates a secure password

    Args:
        length (int): The length of the password
        chars (str): The characters that can be used in the password
    """

    password = ""

    """
    SystemRandom() uses /dev/urandom as a source for random numbers.
    /dev/urandom is cryptographically secure: www.2uo.de/myths-about-urandom
    """
    rand = random.SystemRandom()

    for i in range(shuffle_iterations):
        rand.shuffle(chars)

    for i in range(length):
        c = rand.choice(chars)
        password += c

    return password
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help="How long the generated password should be.", type=int, required=True)
    args = parser.parse_args()

    shuffle_iterations = 100
    password_len = args.length

    numbers = [str(i) for i in range(0,10)]
    all_chars = list(string.ascii_letters + string.punctuation) + numbers
    password = generate_password(password_len, all_chars, shuffle_iterations)
    print(password)

if __name__ == '__main__':
    main()
