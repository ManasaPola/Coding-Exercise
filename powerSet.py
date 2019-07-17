'''This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.'''

def main():
    s = [1,2,3]
    n = len(s)
    pow = 2 ** n
    ans = []
    for counter in range(pow):
        for j in range(n):
            if ((counter & (1 << j))> 0):
                print(counter, j)
                ans.append(s[j])
                print(s[j], end= "")
        print("")

if __name__ == "__main__":
    main()