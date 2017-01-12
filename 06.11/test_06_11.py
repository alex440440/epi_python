import random
import unittest

import math

from exercise_06_11 import Main
from utils import Utils


class Test_06_11(unittest.TestCase):

    def test1(self):
        ar=[1,2,3]
        dir={}
        initial_ar = Utils.clone(ar)
        for i in range(1000*math.factorial(len(ar))):
            Main.get_random_permutation(ar,len(ar)-1)
            hash = Test_06_11.list_hash(self,ar)
            self.add_to_map(dir, hash)
        print(str(dir))

    def add_to_map(self, dir, hash):
        if not dir.has_key(hash):
            dir[hash] = 1
        else:
            dir[hash] += 1

    #python radom is inclusive
    def test2(self):
        max=3
        dir={}
        for i in range(1000*math.factorial(max)):
            self.add_to_map(dir, random.SystemRandom().randint(0,max))
        print(str(dir))

    def list_hash(self, lst):
        return str(lst)

if __name__ == '__main__':
    unittest.main()
