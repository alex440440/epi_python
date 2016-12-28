import sys


class Main:
    @staticmethod
    def find_max(ar):
        max_sum = 0
        min_cost = sys.maxint
        for cost in ar:
            max_sum = max(max_sum, cost - min_cost)
            min_cost = min(min_cost, cost)
        return max_sum

    @staticmethod
    def find_longest_subarray(ar):
        max_sum = 0
        current_length = 0
        prev = None
        for i in ar:
            if i == prev:
                current_length += 1
            else:
                current_length = 1
                prev = i
            max_sum = max(current_length, max_sum)
        return max_sum


if __name__ == "__main__":
    Main().main()
