def main():
    #513 - 5 * f(99) + f(13) + 100
    def count2(n):
        count = 0
        length = len(str(n))
        for i in range(length):
            count += count2digit(n , i)
        print(count)

    def count2digit(n , d):
        pow10 = 10 ** d
        nextPow10 = pow10 * 10
        right = n % pow10

        roundDown = n - n % nextPow10
        roundUp = roundDown + nextPow10

        digit = (n // pow10) % 10
        print(digit, roundUp, roundDown)

        if digit < 2:
            return roundDown // 10
        if digit == 2:
            return roundDown // 10 + right + 1
        else:
            return roundUp // 10

    count2(100)





if __name__ == "__main__":
    main()