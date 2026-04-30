def isValidBST(root):
        def dfs(node, high, low):
            if not node:
                return True

            if not (node.val < high and node.val > low):
                return False

            return (dfs(node.left, node.val, low) and dfs(node.right, high, node.val))

        return dfs(root, float("inf"), float("-inf"))
