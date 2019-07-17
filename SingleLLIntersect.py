'''Daily Coding problem - 20

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.'''

def main(headA, headB):
    currA = headA
    hashA = set()
    while currA:
        hashA.add(currA)
        # print(currA.val)
        currA = currA.next

    currB = headB
    while currB:
        if currB in hashA:
            return currB
        currB = currB.next
    return None

if __name__ == "__main__":
    main()