
def main():
    a = 2437
    b = 875
    x = a
    y = b
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    print(x)

if __name__ == "__main__":
    main()