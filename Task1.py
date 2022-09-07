""" Task 1. You have a positive integer number N as an input. 
Please write a program in Python 3 that calculates the sum in range 1 and N."""

import numpy as np
import time
import argparse

def calculate_sum(N=10):
    program_starts = time.time()
    print(f"Sum in range 1 and {N} =", np.arange(1, N+1, dtype=np.longlong).sum())
    now = time.time()
    print(f"It has been {now - program_starts} seconds since the loop started")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program calculates sum of integers in range 1 and N.')
    parser.add_argument('N', metavar='N', type=int,
                    help='a positive integer')
    args = parser.parse_args()
    if args.N > 0 and args.N < 10e25:
        calculate_sum(args.N)
    else:
        parser.error("Non positive value of N")

    