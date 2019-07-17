
def main():
    str1 = "gcddllldk"
    str2 = "gcd"
    count1 = [0] * 26
    count2 = [0] * 26

    for char in str1:
        count1[ord(char)-ord('a')] += 1

    for char in str2:
        count2[ord(char)-ord('a')] += 1

    result = 0
    for i in range(26):
        result += abs(count1[i]-count2[i])

    print(result)

if __name__ == "__main__":
    main()