def main():
    inputStr = "babad"
    maxLength = 0
    startIndex = 0
    endIndex = 0
    for i in range(len(inputStr)):
        len1 = eCenter(inputStr, i, i)
        len2 = eCenter(inputStr, i, i+1)
        l = max(len1, len2)
        if maxLength < l:
            maxLength = l
            startIndex = i - (l-1)//2
            # print(startIndex)
            endIndex = i + (l)//2+1
            # print(endIndex)
    print(inputStr[startIndex:endIndex])

def eCenter(s, i, j):
    while i>=0 and j<len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return j - i - 1


if __name__ == "__main__":
    main()