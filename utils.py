
#Uitls.py

import random

class Utils:

    @staticmethod
    def swap(array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    @staticmethod
    def clone(array):
        return array[0:len(array)]

    @staticmethod
    def random(max):
        if max==0:
            return 0
        return random.SystemRandom().randint(0,max)