import sys


class Main:
    # @staticmethod
    # def apply_permutation_simple(array,permutation):
    #     out=[''] * len(array)
    #     count=0
    #     for i in xrange(len(array)):
    #         out[permutation[i]]=array[i]
    #     return out

    # also O(n) - because is changing the permutation array and there is no way to restore it.
    # @staticmethod
    # def apply_permutation(array, permutation):
    #     for i in xrange(len(array)):
    #         Main.swap(array, i, permutation[i])
    #         Main.swap(permutation, i, permutation[i])
    #     return array

    @staticmethod
    def apply_permutation(array, permutation):
        print("permutation: "+str(permutation))

        array_length = len(array)
        for cycle_start in xrange(array_length):
            # initial index of the cycle
            move_from = cycle_start
            # get the index we need to move the first member of the cycle
            move_to = permutation[move_from]
            permutation[move_from] -= array_length
            while (True):
                print("cycle_start: "+str(cycle_start)+", move_from: "+str(move_from)+", move_to: "+str(move_to))
                print("permutation: "+str(permutation))

                # we go in a cyclical fashion to the next member we can move,
                # till we arrive to the member that should be moved to the place of one we already moved
                # if it's the case, we arrived to the cycle end and should move to the next cycle.
                is_new_permutation = move_to >= 0
                if is_new_permutation:
                    print("We are looking at a permutation which was not yet performed")

                    # swap here
                    # move_from -> move_to
                    # move_to -> move_from
                    Main.swap(array, move_from, move_to)


                    # we just swapped this member with the one we placed from move_from,
                    # so the next member we are going to move is the misplaced one at move_from
                    # and its destination is stored in the permutation array where he was before we swapped it - move_to
                    old_permutation_index=move_to
                    move_to = permutation[move_to]

                    # mark the permutation as one we already performed
                    permutation[old_permutation_index] -= array_length
                else:
                    print("We are looking at a permutation which was already performed, let's move on")
                    break

        # restore permutation values
        for p in permutation:
            p += array_length

        return array

    # @staticmethod
    # def inverse_permutation(permutation):
    #     value = 0
    #     while value >= 0:
    #         print("checking for i: " + str(value) + ":" + str(permutation[value]))
    #         index = permutation[value]
    #         tmp_value = permutation[index]
    #         permutation[index] = -value
    #         value = tmp_value
    #
    #     for i in range(len(permutation)):
    #         permutation[i] = -permutation[i]
    #
    #     return permutation

    @staticmethod
    def get_zero(permutation):
        return -len(permutation)

    @staticmethod
    def swap(array, i, j):
        print ("swapping "+array[i]+":"+str(i)+" with "+array[j]+":"+str(j))
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp


if __name__ == "__main__":
    Main().main()
