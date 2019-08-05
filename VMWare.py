from collections import defaultdict
def main():
    s = ["code", "doce", "ecod", "framer", "frame"]
    #wordMap = defaultdict(list)
    wordMap = {}
    ans = []
    for word in s:
        sortedWord = sorted(word)
        sortedWord = "".join(sortedWord)
        if sortedWord not in wordMap:
            wordMap[sortedWord] = word

    for key in wordMap:
        ans.append(wordMap[key])
    print(ans)

if __name__ == "__main__":
    main()