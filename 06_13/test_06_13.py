import unittest

import math

from exercise_06_13 import Main
from utils import Utils


class Test_06_13(unittest.TestCase):

    def test1(self):
        out=Main.get_random_permutations(10)
        print(str(out))

    def test2(self):
        n=5
        map={}
        permutation_count = math.factorial(n)
        for i in xrange(permutation_count):
            self.add_to_map(map,self.get_different_permutations_for_n(n))
        for key in sorted(map):
            print(str(key) +":" + str(map[key]) +", probability is " + str(self.p_k_from_n_are_full(key, permutation_count)))


    def get_different_permutations_for_n(self, n):
        map={}
        for i in xrange(math.factorial(n)+1):
             self.add_to_map(map,self.list_hash(Main.get_random_permutations(n)))
        # print "got "+str(len(map)) +" different permutation of "+str(n)
        return len(map)

    def test3(self):
        n=5
        map={}
        permutation_count = math.factorial(n)
        for i in xrange(permutation_count+1):
            print("probability: " + str(i) +":" + str(self.p_k_from_n_are_full(i, permutation_count)))


    def choose_k_from_n(self, n, k):
        # 0 <= k <= n
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


    def p_j_from_n_are_full_after_k_attempts(self, j, k, n):
        #  0 <= j <= k, j <= n
        x = 0
        for t in range(j):
            x = x + self.choose_k_from_n(j, t) * ((-1) ** (t)) * ((j - t) ** k)
        return x*self.choose_k_from_n(n, j)

    def p_k_from_n_are_full(self, k, n):
        return (self.p_j_from_n_are_full_after_k_attempts(k, n, n) + 1.0) / n ** n


    def add_to_map(self, dict, hash):
        if not dict.has_key(hash):
            dict[hash] = 1
        else:
            dict[hash] += 1

    def list_hash(self, lst):
        return str(lst)

if __name__ == '__main__':
    unittest.main()
