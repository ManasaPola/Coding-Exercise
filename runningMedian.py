'''This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2'''
def main():
    input = [2, 1, 5, 7, 2, 0, 5]
    num = 2
    obj = MedianFinder()
    obj.addNum(num)
    param_2 = obj.findMedian()


import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if len(self.small) > len(self.big):
            if num >= self.findMedian():
                heapq.heappush(self.big, num)
            else:
                # print(self.small)
                x = -heapq.heappushpop(self.small, -num)

                print(x)
                heapq.heappush(self.big, x)
                print(self.big)
        else:
            if num <= self.findMedian():
                heapq.heappush(self.small, -num)
            else:
                y = heapq.heappushpop(self.big, num)
                heapq.heappush(self.small, -y)

    def findMedian(self) -> float:
        if not self.small:
            return 0
        elif len(self.small) > len(self.big):
            # print(self.small)
            # print(-self.small[0])
            return -self.small[0] / 1.0
        else:
            return (-self.small[0] + self.big[0]) / 2


if __name__ == "__main__":
    main()