def main():
    k = 10
    pow2 = 0
    pow3 = 0
    pow7 = 0
    seq = [1]

    while k > 0:
        a, b, c = 2 * seq[pow2], 3 * seq[pow3], 7 * seq[pow7]
        m = min(a, b, c)
        print(m)
        if m == a:
            pow2 += 1
        if m == b:
            pow3 += 1
        if m == c:
            pow7 += 1
        seq.append(m)
        k -= 1

    print(m)




if __name__ == "__main__":
    main()