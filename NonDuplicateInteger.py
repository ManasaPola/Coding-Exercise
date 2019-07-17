'''This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
6, 3, 3, 3, 1, 6, 6,
6, 9, 12, 15, 16, 22, 28
Do this in O(N) time and O(1) space.'''
def main():
    input = [6, 3, 4, 4, 4, 6, 6]
    runningSum = 0
    for n in input:
        runningSum += n
    print(runningSum / 3)
    print(runningSum - (runningSum // 3) )



if __name__ == "__main__":
    main()