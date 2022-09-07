""" Task 2. You have a matrix MxN that represents a map. 
There are 2 possible states on the map: 1 - islands, 0 - ocean. 
Your task is to calculate the number of islands in the most effective way. """

import numpy as np
import argparse


def calculate_islands(array):
    k = 2 # running variable
    Mk = {}
    N = array.copy()
    
    ''' The Hoshen-Kopelman Algorithm '''
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if N[i][j] > 0:
                if (i == 0 or N[i - 1][j] == 0) and (j == 0 or N[i][j - 1] == 0):
                    k += 1
                    N[i][j] = k
                    Mk[k] = 1
                elif (i > 0 and N[i - 1][j] > 0) and (j == 0 or N[i][j - 1] == 0):
                    N[i][j] = N[i - 1][j]
                    Mk[N[i - 1][j]] += 1
                elif (j > 0 and N[i][j - 1] > 0) and (i == 0 or N[i - 1][j] == 0):
                    N[i][j] = N[i][j - 1]
                    Mk[N[i][j - 1]] += 1
                elif (j > 0 and N[i][j - 1] > 0) and (i > 0 and N[i - 1][j] > 0) and (
                        N[i][j - 1] != N[i - 1][j]):
                    N[i][j] = N[i][j - 1]
                    Mk[N[i][j - 1]] = Mk[N[i][j - 1]] + Mk[N[i - 1][j]] + 1
                    Mk[N[i - 1][j]] = 0
                elif (j > 0 and N[i][j - 1] > 0) and (i > 0 and N[i - 1][j] > 0) and (
                        N[i][j - 1] == N[i - 1][j]):
                    N[i][j] = N[i][j - 1]
                    Mk[N[i][j - 1]] += 1
    return len({key: value for key, value in Mk.items() if value != 0})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program calculates the number of islands on a MxN map'+
                                                '\nrandomly located 1-island and 0-ocean.')
    parser.add_argument('M', metavar='M', type=int,
                    help='width of map')
    parser.add_argument('N', metavar='N', type=int,
                    help='height of map')
    args = parser.parse_args()
    
    if args.M > 0 and args.N > 0:
        array_map = np.random.randint(2, size=args.M*args.N).reshape((args.M, args.N))
        print(array_map)
        no_of_islands = calculate_islands(array_map)
        print(f"There are {no_of_islands} islands on this map.")
    else:
        parser.error("Non positive value of M or N")