import sys


class Main:

    @staticmethod
    def get_primes(number):
        return Main.get_primes_sieving(number)

    @staticmethod
    def get_primes_division(number):
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

    @staticmethod
    def get_primes_sieving(number):
        primes=[]
        is_prime = [True] * number
        is_prime[1] = False
        for num in xrange(2, number):
            if is_prime[num]:
                primes.append(num)
                for i in xrange(num,number,num):
                    is_prime[i]=False
        return primes

if __name__ == "__main__":
    Main().main()
