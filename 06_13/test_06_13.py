import unittest

import math

from exercise_06_13 import Main
from utils import Utils


class Test_06_13(unittest.TestCase):

    def test1(self):
        ar=[1,2,3]
        dir={}
        initial_ar = Utils.clone(ar)
        for i in range(1000*math.factorial(len(ar))):
            Main.permute(ar)
            hash = Test_06_13.list_hash(self,ar)
            if not dir.has_key(hash):
                dir[hash]=1
            else:
                dir[hash]+=1
        print(str(dir))

    def list_hash(self, lst):
        return str(lst)

if __name__ == '__main__':
    unittest.main()
