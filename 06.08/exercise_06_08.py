import sys


class Main:

    @staticmethod
    def get_primes(number):
        primes=[]
        for num in xrange(2,number+1):
            if not Main.is_divisable(num, primes):
                primes.append(num)
        return primes


    @staticmethod
    def is_divisable(number, primes):
        for prime in primes:
            # print("checking primeness for "+str(prime))
            if number % prime == 0 and prime != 1:
                return True
        return False


if __name__ == "__main__":
    Main().main()
