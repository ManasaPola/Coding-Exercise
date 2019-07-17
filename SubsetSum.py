class Subset:
    res = []
    def __init__(self, nums, target):
        self.input = nums
        self.target = target
        self.used = [0] * len(self.input)

    def sum(self):
        self.subsetSum(self.input, 0, 0, self.target, self.used)
        return res

    def subsetSum(self, nums, currSum , index, sum, used):
        if currSum == sum:
            global res
            res = []
            for i in range(len(used)):
                if used[i] == 1:
                    res.append(nums[i])
            return
        elif index == len(nums):
            return
        else:
            used[index] = 1
            self.subsetSum(nums, currSum + nums[index], index+1, sum, used)
            used[index] = 0
            self.subsetSum(nums, currSum, index+1, sum, used)

def main():
    input = [12, 1, 61, 5, 9, 2]
    # used = [0] * len(input)
    s = Subset(input, 24)
    print(s.sum())

if __name__ == "__main__":
    main()