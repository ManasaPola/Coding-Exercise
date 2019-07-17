from collections import defaultdict
import copy
def main():
    word = "CYCLE"
    tup = [('C', 'B'), ('Y', 'C'), ('C', 'E'), ('L', 'R'), ('C', 'R')]

    wordmap = {}

    for char in word:
        temp = []
        for i, t in enumerate(tup):
            if char in t:
                temp.append(i)
        wordmap[char] = temp

    ans = [False]
    visited = [0] * len(tup)

    def find(word, index, visited):
        if index == len(word):
            ans[0] = True
            return
        l = wordmap.get(word[index])
        # print(l)
        for i in l:
            if visited[i] != -1:
                # print(word[index], i)
                visited[i] = -1
                find(word, index+1, visited)
                visited[i] = 0
            else:
                continue

    find(list(word), 0, visited)
    print(ans[0])

if __name__ == "__main__":
    main()