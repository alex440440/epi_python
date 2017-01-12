import random
import sys

from utils import Utils


class Main:

    @staticmethod
    def permute(ar):
        for i in xrange(0,len(ar)):
            max_rand=len(ar)-1-i  # in Python random values include max
            Utils.swap(ar,i,i+random.SystemRandom().randint(0,max_rand))


    # @staticmethod
    # def __run_permutation(ar, start, end):
    #     length = end-start
    #     if length==0:
    #         return
    #     Main.__run_permutation(ar,start,end-1)
    #     random_normalized = Utils.random(ar) % length - 1
    #     Utils.swap(ar, random_normalized, end)



if __name__ == "__main__":
    Main().main()
