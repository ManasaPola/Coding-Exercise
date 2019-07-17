'''This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.'''
def main():
    print('H')

if __name__ == "__main__":
    main()

class Record:
    def __init__(self, n):
        self.stack = []
        self.maxSize = n
        self.currIndex = 0

    def record(self, val):
        self.stack[self.currIndex] = val
        self.currIndex = (self.currIndex + 1) % self.maxSize

    def get_last(self, i):
        return self.stack[(self.currIndex - i + self.maxSize) % self.maxSize]