import sys


class Main:

    @staticmethod
    def find_max_twice(ar):
        forward_sum = Main.forward_sweep(ar)
        backward_sum=Main.backward_sweep(ar)
        length = len(forward_sum)
        back_rev = backward_sum[::-1]
        return max([forward_sum[i]+back_rev[i] for i in xrange(length)])

    @staticmethod
    def forward_sweep(ar):
        max_sums = []
        max_sum = 0
        min_cost = sys.maxint
        for cost in ar:
            max_sum = max(max_sum, cost - min_cost)
            if cost < min_cost:
                min_cost = cost
            max_sums.append(max_sum)
        return max_sums

    @staticmethod
    def backward_sweep(ar):
        max_sums = []
        max_sum = 0
        max_cost = -sys.maxint
        for cost in reversed(ar):
            if cost > max_cost:
                max_cost = cost
            max_sum = max(max_sum, max_cost-cost)
            max_sums.append(max_sum)
        return max_sums

if __name__ == "__main__":
    Main().main()
