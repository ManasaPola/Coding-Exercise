""" Daily Coding problem #22 Medium
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']."""
def main():
    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    sentence = "bedbathandbeyond"
    valid = []
    def backtrack(sentence, words, currWords):
        if len(sentence) == 0:
            valid.append(currWords)

        currString = ""
        for i in range(len(sentence)):
            currString += sentence[i]
            if currString in words:
                backtrack(sentence[i+1:], words, currWords + [currString])

    backtrack(sentence, words, [])
    print(valid)


if __name__ == "__main__":
    main()