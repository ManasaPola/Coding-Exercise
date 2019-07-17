'''Daily coding problem 29
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters
as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of
alphabetic characters. You can assume the string to be decoded is valid.'''

def main():
    inputStr = "AAAABBBCCDAA"
    outputStr = ""
    count = 1
    for i in range(1, len(inputStr)):
        if inputStr[i-1] != inputStr[i]:
            outputStr += str(count)
            outputStr += inputStr[i-1]
            count = 1
        else:
            count += 1
    if count > 1:
        outputStr += str(count)
        outputStr += inputStr[i]
    # print(outputStr)
    print(inplace(inputStr))

def inplace(inputStr):
    index = 0
    anchor = 0
    inputStr = list(inputStr)
    #print('Hello')
    for i, c in enumerate(inputStr):
        if i+1 == len(inputStr) or c != inputStr[i+1]:
            print(i, anchor)
            if i > anchor:
                for digit in str(i - anchor + 1):
                    inputStr[index] = digit
                    index += 1
            inputStr[index] = inputStr[anchor]
            index += 1
        anchor = i + 1
    # if count > 1:
    #     for digit in str(count):
    #         inputStr[index] = digit
    #         index += 1
    #     inputStr[index] = inputStr[i - 1]
    #     index += 1
    #     count = 1
    return "".join(inputStr[:index])

if __name__ == "__main__":
    main()