def main():
    input = "AAB"
    N = len(input)
    count = 0
    for i in range(0, N):
        for j in range(i+1, N+1):
            count += 1
    print(count)

if __name__ == "__main__":
    main()