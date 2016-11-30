import unittest
from e_6_6_0 import Main


class Test_660(unittest.TestCase):

    def test1(self):
        ar = [4, 5, 6, 10]
        find_max = Main.find_max(ar)
        print("find_max: ", find_max)
        self.assertEqual(find_max, 6)


    def test2(self):
        ar = [310,315,275,295,260,270,290,230,255,250]
        find_max = Main.find_max(ar)
        print("find_max: ", find_max)
        self.assertEqual(find_max, 30)

if __name__ == '__main__':
    unittest.main()