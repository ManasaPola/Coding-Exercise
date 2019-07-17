'''This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.'''

def main():
    ans = True
    inputStr = "]"
    stack = []
    for char in inputStr:
        if char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                ans = False
                break
        elif char == '}':
            if len(stack) == 0 or stack.pop() != '{':
                ans = False
                break
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                ans = False
                break
        else:
            stack.append(char)
    if len(stack) > 0:
        ans = False
    print(ans)



if __name__ == "__main__":
    main()