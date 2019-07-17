'''Leetcode Contest'''

def main():
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    text1 = "we will we will rock you"
    first1 = "we"
    second1 = "will"
    ans = findOccurences(text1, first1, second1)
    print(ans)

def findOccurences(text, first, second):
    if len(text) == 0:
        return []
    words = text.split(" ")
    ans = []
    for i in range(0, len(words)-2):
        if words[i] == first and words[i+1] == second:
            ans.append(words[i+2])
    return ans

if __name__ == "__main__":
    main()