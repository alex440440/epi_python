import random
import sys

sys.path.insert(0, '../06_11')

import exercise_06_11


class Main:

    @staticmethod
    def get_random_permutations(n):
        permutations=[]
        for i in xrange(n):
            permutations.append(i)
        exercise_06_11.Main.get_random_permutation(permutations,n)
        return permutations

if __name__ == "__main__":
    Main().main()
