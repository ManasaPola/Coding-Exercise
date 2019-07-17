'''
#12
Amazon
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''


def main():
    f = {}
    f[1] = 1
    f[0] = 1
    def steps(N, l):
        if N < 0:
            return 0
        elif N in f:
            return f[N]

        ans = 0
        for step in l:
            ans += steps(N-step, l)
        f[N] = ans
        return ans

    l = [1,3,5]
    a = steps(10, l)
    print(a)

if __name__ == "__main__":
    main()
