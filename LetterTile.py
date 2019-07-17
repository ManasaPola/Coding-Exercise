
def main():
    tiles = "AAABBC"
    ans = numTilePossibilities(tiles)
    print(ans)

def numTilePossibilities(tiles):
    substringSet = set()
    n = len(tiles)
    for i in range(n):
        for j in range(i+1, n+1):
            substringSet.add(tiles[i:j])

    totalCount = 0
    for s in substringSet:
        l = len(s)
        freq = [0] * 26
        for i in range(0, l):
            if (s[i] >= 'A') :
                freq[(ord)(s[i]) - 65] = freq[(ord)(s[i]) - 65] + 1
        fact = 1
        for i in range(26):
            fact = fact * factorial(freq[i])
        totalCount += factorial(l) // fact

    return totalCount

def factorial(l):
    fact = 1
    for i in range(2, l+1):
        fact = fact * i
    return fact



if __name__ == "__main__":
    main()