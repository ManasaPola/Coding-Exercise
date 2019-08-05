import math
def main():
    dig = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]
    ans = ["0"]

    def lastNon0Digit(n):
        if (n < 10):
            return dig[n]

        if (((n // 10) % 10) % 2 == 0):
            return (6 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
        else:
            return (4 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
        return 0

    # driver code
    n = 2017

    print(lastNon0Digit(n))





if __name__ == "__main__":
    main()