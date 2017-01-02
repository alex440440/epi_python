import unittest
from exercise_06_08 import Main

class Test_06_08(unittest.TestCase):

    def test1(self):
        primes = Main.get_primes(18)
        print ("primes are "+str(primes))
        self.assertEqual(primes, [2,3,5,7,11,13,17])

if __name__ == '__main__':
    unittest.main()
