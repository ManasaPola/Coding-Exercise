class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
    # Compare the new value with the parent node
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

def main():
    root = Node(0)
    root.insert(1)
    root.insert(0)
    root.insert(1)
    root.insert(1)
    root.insert(0)
    root.PrintTree()
    # print(dfs(root))

def dfs(root) -> int:
    count = 0
    if root:
        dfs(root.left)
        if root.left is None and root.right is None:
            count += 1
        elif root.val == root.left.val and root.val == root.right.val:
            count += 1
        dfs(root.right)
    return count


if __name__ == "__main__":
    main()