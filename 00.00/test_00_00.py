import unittest
from exercise_00_00 import Main

class Test_00_00(unittest.TestCase):

    def test1(self):
        a=1
        out=Main.method(a)
        print("out: ", out)
        self.assertEqual(out, 1)

if __name__ == '__main__':
    unittest.main()
