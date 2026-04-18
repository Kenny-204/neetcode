import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


def rightSideView(root):
    if not root:
        return []
    queue = collections.deque()
    queue.append(root)
    res = []
    while queue:
        queLen = len(queue)
        for i in range(queLen):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if i == (queLen-1):
                res.append(node.val)
    return res

print(rightSideView(root))
