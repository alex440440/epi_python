import sys


class Main:
    @staticmethod
    def find_max(ar):
        max_sum = 0;
        min_cost = sys.maxint
        for cost in ar:
            max_sum = max(max_sum, cost - min_cost)
            min_cost = min(min_cost, cost)
        return max_sum


if __name__ == "__main__":
    Main().main()
