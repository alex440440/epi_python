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
    def apply_permutation(array, permutations):
        for i in xrange(len(array)):
            Main.swap(array,i,permutations[i])
            Main.swap(permutations,i,permutations[i])
        return array


    @staticmethod
    def swap(array, i, j):
        tmp = array[i]
        array[i]=array[j]
        array[j]=tmp

if __name__ == "__main__":
    Main().main()
