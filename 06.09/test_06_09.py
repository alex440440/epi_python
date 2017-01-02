import unittest
from exercise_06_09 import Main

class Test_06_09(unittest.TestCase):

    def test1(self):
        out = Main.apply_permutation(['a','b','c','d'],[2,0,1,3])
        print ("permutations are "+str(out))
        self.assertEqual(out, ['b','c','a','d'])

    def test2(self):
        out = Main.apply_permutation(['a','b','c','d'],[3,2,1,0])
        print ("permutations are "+str(out))
        self.assertEqual(out, ['d','c','b','a'])

    def test3(self):
        array = ['a', 'b', 'c', 'd']
        array_copy= array[:]
        permutation = [3, 2, 1, 0]
        permutation_copy = permutation[:]
        permuted = Main.apply_permutation(array, permutation)
        back = Main.apply_permutation(permuted,Main.inverse_permutation(permutation_copy))
        print ("permutations are "+str(back))
        self.assertEqual(back,array_copy)



if __name__ == '__main__':
    unittest.main()
