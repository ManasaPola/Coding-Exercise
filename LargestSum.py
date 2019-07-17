'''This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.'''

def main():
    input = [7, 800, 3, -1, -100, -10]
    f0 = 0
    f1 = 0
    totalMax = 0
    for n in input:
        f2 = max(n+f0, f1)
        f0 = f1
        f1 = f2

    print(f2)


if __name__ == "__main__":
    main()