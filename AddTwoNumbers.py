def main():
    a = 5
    b = 3

    def recurse(a, b):
        print(a, b)
        if b == 0:
            print(a)
            return
        x = a ^ b
        y = (a & b) << 1
        recurse(x, y)

    recurse(a, b)


if __name__ == "__main__":
    main()