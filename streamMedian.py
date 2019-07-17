import heapq
class Median:
    def __init__(self):
        self.small = []
        self.big = []

    def push(self, val):
        if len(self.small) > len(self.big):
            if val >= self.getMedian():
                heapq.heappush(self.big, val)
            else:
                num = heapq.heappushpop(self.small, -val)
                heapq.heappush(self.big, num)
        else:
            if val <= self.getMedian():
                heapq.heappush(self.small, -val)
            else:
                lastElement = heapq.heappushpop(self.big, val)
                heapq.heappush(self.small, -lastElement)

    def getMedian(self):
        if not self.small:
            return 0
        elif len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0])/ 2

def main():
    obj1 = Median()
    obj1.push(2)
    obj1.push(3)
    print(obj1.getMedian())


if __name__ == "__main__":
    main()