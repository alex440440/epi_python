import sys

class Main:

    # @staticmethod
    # def apply_permutation_simple(array,permutation):
    #     out=[''] * len(array)
    #     count=0
    #     for i in xrange(len(array)):
    #         out[permutation[i]]=array[i]
    #     return out

    @staticmethod
    def apply_permutation(array, permutation):
        for i in xrange(len(array)):
            Main.swap(array, i, permutation[i])
            Main.swap(permutation, i, permutation[i])
        return array

    @staticmethod
    def inverse_permutation(permutation):
        apply_permutation = Main.apply_permutation(permutation, permutation)
        return apply_permutation[::-1]


    @staticmethod
    def swap(array, i, j):
        tmp = array[i]
        array[i]=array[j]
        array[j]=tmp

if __name__ == "__main__":
    Main().main()
