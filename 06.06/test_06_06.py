import unittest
from exercise_06_06 import Main

class Test_660(unittest.TestCase):

    def test1(self):
        ar = [4, 5, 6, 10]
        find_max = Main.find_max(ar)
        print("find_max: ", find_max)
        self.assertEqual(find_max, 6)

    def test2(self):
        ar = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        find_max = Main.find_max(ar)
        print("find_max: ", find_max)
        self.assertEqual(find_max, 30)

    def test3(self):
        ar = [1,2,3,4,5]
        longest = Main.find_longest_subarray(ar)
        print("longest: ", longest)
        self.assertEqual(longest, 1)

    def test4(self):
        ar = [1,1,1,2,3,4,4,5,5]
        longest = Main.find_longest_subarray(ar)
        print("longest: ", longest)
        self.assertEqual(longest, 3)


    def test5(self):
        ar = [1,1,1,2,3,4,4,5,5,5,5]
        longest = Main.find_longest_subarray(ar)
        print("longest: ", longest)
        self.assertEqual(longest, 4)

if __name__ == '__main__':
    unittest.main()
