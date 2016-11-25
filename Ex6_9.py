class MyClass:
    def get_deltas(self, ar):
        ret = []
        for i in range(len(ar) - 1):
            ret.append(ar[i + 1] - ar[i])
        return ret

    def find_max(self, ar, k):
        deltas = self.get_deltas(ar)
        max_sum = 0;
        current_sum = 0;
        left = 0;
        right = 0;

        for i in range(len(deltas)):
            current_sum = max(current_sum + deltas[i], deltas[i])
            print("i:", i, ", current_sum: ", current_sum)
            if current_sum > max_sum:
                max_sum = current_sum
                right = i + 1
            if current_sum == deltas[i]:
                left = i
        return max_sum, left, right

    def __init__(self):
        self.find_max
        self.get_deltas


if __name__ == "__main__":
    MyClass().main()
