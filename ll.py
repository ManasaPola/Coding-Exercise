import collections
def main():
    input_string = input("Enter a list element separated by space ")
    strList = input_string.split()
    l = []
    for s in strList:
        l.append(int(s))
    tempD = input("Enter d value ")
    d = int(tempD)
    q = collections.deque(l)
    for i in range(0, d):
        a = q.popleft()
        q.append(a)
    print(q)
    return q
# stack = []
    # l = [1, 2, 3, 4, 5]
    # d = 4

if __name__ == "__main__":
    main()