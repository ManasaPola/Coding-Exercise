'''Daily Coding problem 26
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.'''

def main(head):
    last = head
    klast = head
    count = 0
    k = 4
    while count < k:
        last = last.next
        count += 1
    # print(count)
    prev = None
    # if last is None:
    #     return None
    while last:
        prev = klast
        klast = klast.next
        last = last.next
    # print(klast.val)
    if prev:
        prev.next = klast.next
    else:
        return klast.next
    return head

if __name__ == "__main__":
    main()