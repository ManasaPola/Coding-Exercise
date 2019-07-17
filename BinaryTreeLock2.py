class Node:
    def __init__(self, val, parent=None,left=None, right= None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False

    def checkAncestor(self):
        if self.locked:
            return False

        if self.parent == None:
            return True

        return self.parent.checkAncestor()

    def checkDescendants(self):
        if self.locked:
            return False

        return (not self.left or self.left.checkDescendants()) and (not self.right or self.right.checkDescendants())

    def lock(self):
        if self.locked:
            return False

        if (not self.parent or self.parent.checkAncestor()) or ((not self.left or self.left.checkDescendants()) and (not self.right or self.right.checkDescendants())):
            self.locked = True
            print("Locked " + str(self))
            # print("Locked " + str(self))
            return True

        print("Cannot Lock "+ str(self))
        return False

    def unlock(self):
        if self.locked == False:
            return False

        if (not self.parent or self.parent.checkAncestor()) or (
                (not self.left or self.left.checkDescendants()) and (not self.right or self.right.checkDescendants())):
            self.locked = False
            print("UnLocked " + str(self))
            return True

        print("Cannot UnLock " + str(self))
        return False



if __name__ == "__main__":
    """
               4
              / \
             2   5
            / \
           1   3
          /
         0
        """

    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    four.left = two
    two.parent = four

    four.right = five
    five.parent = four

    two.left = one
    one.parent = two

    two.right = three
    three.parent = two

    one.left = zero
    zero.parent = one

    two.lock()
    zero.lock()
    one.lock()
    zero.unlock()
    one.lock()
    zero.lock()
    one.unlock()
    two.unlock()
    one.unlock()
    zero.unlock()