import unittest
from exercise_06_09 import Main

class Test_06_09(unittest.TestCase):

    def test1(self):
        out = Main.apply_permutation(['a', 'b', 'c', 'd'], [2, 0, 1, 3])
        print ("permutations are " + str(out))
        self.assertEqual(out, ['b', 'c', 'a', 'd'])

    def test2(self):
        out = Main.apply_permutation(['a', 'b', 'c', 'd'], [3, 2, 1, 0])
        print ("permutations are " + str(out))
        self.assertEqual(out, ['d', 'c', 'b', 'a'])

    def test3(self):
        out = Main.apply_permutation(['a', 'b', 'c', 'd', 'e'], [2, 1, 0, 4, 3])
        print ("permutations are " + str(out))
        self.assertEqual(out, ['c', 'b', 'a', 'e', 'd'])


    def test4(self):
        permutation = [2,0,1,3]
        Main.inverse_permuatation(permutation)
        self.assertEquals(permutation, [1,2,0,3])


if __name__ == '__main__':
    unittest.main()
