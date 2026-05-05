# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(7)

root.left = TreeNode(5)
root.right = TreeNode(9)

root.left.left = TreeNode(3)
root.left.right = TreeNode(6)

root.right.left = TreeNode(8)
root.right.right = TreeNode(10)


def buildTree(preorder, inorder):
    if not preorder:
        return None

    root = preorder[0]
    mid = inorder.find(preorder[0])

    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root

buildTree(root)
