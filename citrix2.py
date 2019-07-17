import math
def main():
    count = 0

    def perfectSquare(number):
        root = math.sqrt(number)
        if int(root + 0.5) ** 2 == number:
            return True
        else:
            return False

    numbers = [1,2,3,4,5]

    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            if perfectSquare(numbers[i] + j):
                print(numbers[i], j)
                count += 1
    print(count)


if __name__ == "__main__":
    main()