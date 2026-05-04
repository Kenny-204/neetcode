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


# def kthSmallest(root, k):
#     res = 0
#     stack = []
#     visited = {}
#     curr = root
#     while curr or stack:
#         stack.append(curr)
#         if curr.left and curr.left not in visited:
#             curr = curr.left
#         else:
#             res += 1
#             processing = stack.pop()
#             if res == k:
#                 return processing.val
#             visited[processing] = True
#             if processing.right:
#                 curr = processing.right
#             else:
#                 if stack:
#                     curr = stack.pop()
#                 else:
#                     break


# print(kthSmallest(root, 2))


def kthSmallest(root, k):
    res = 0
    stack = []
    curr = root
    while curr or stack:
        # go to the leftest end
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        # process current
        res += 1
        if res == k:
            return curr.val

        # go right
        curr = curr.right


print(kthSmallest(root, 2))
