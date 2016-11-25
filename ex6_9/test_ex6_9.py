import unittest
from ex6_9 import MyClass

class TestStringMethods(unittest.TestCase):
    my_class = MyClass()

    def test_deltas(self):
        ar = [1, 2, 3]
        deltas = self.my_class.get_deltas(ar)
        self.assertEquals(deltas, [1, 1])


    def test1(self):
        ar = [4,5,6,10]
        find_max = self.my_class.find_max(ar, 1)
        print("find_max: ", find_max)
        self.assertEqual(find_max, (6, 0, 3))


    def test2(self):
        ar = [2,3,4,5,4,3,2,0,1,15,3,15,0]
        find_max = self.my_class.find_max(ar, 1)
        print("find_max: ", find_max)
        self.assertEqual(find_max, (15, 7, 9))


if __name__ == '__main__':
    unittest.main()