import unittest
from exercise_06_07 import Main

class Test_06_07(unittest.TestCase):

    def test1(self):
        ar = [1,3,1,5]
        find_max = Main.find_max_twice(ar)
        print("find_max: ", find_max)
        self.assertEqual(find_max, 6)

    def test2(self):
        ar = [1,2,1,2,3,10,100,1000]
        find_max = Main.find_max_twice(ar)
        print("find_max: ", find_max)
        self.assertEqual(find_max, 1000)

if __name__ == '__main__':
    unittest.main()
