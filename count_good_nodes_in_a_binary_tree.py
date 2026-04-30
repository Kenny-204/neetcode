import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)

root.left = TreeNode(3)
# root.right = TreeNode(1)

root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)


def goodNodes(root):
    def dfs(node,maxValue):
        if not node:
            return 0
        
        res = 1 if node.val >= maxValue else 0
        maxValue = max(node.val,maxValue)
        res+= dfs(node.left,maxValue)
        res+= dfs(node.right,maxValue)
        return res
        
    
    return dfs(root,root.val)


print(goodNodes(root))
