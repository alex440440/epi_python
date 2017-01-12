import random
import sys

from utils import Utils


class Main:
    @staticmethod
    def get_random_permutation(ar,k):
        for i in xrange(0,k):
            max_rand=len(ar)-1-i  # in Python random values include max
            Utils.swap(ar,i,i+random.SystemRandom().randint(0,max_rand))


if __name__ == "__main__":
    Main().main()
