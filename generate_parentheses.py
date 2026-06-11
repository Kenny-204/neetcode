def generateParenthesis(n):
    res = []

    subset = []

    def backtracking(openno, closeno):
        if openno == closeno == n:
            res.append("".join(subset.copy()))
            return

        if openno < n:
            subset.append("(")
            backtracking(openno + 1, closeno)
            subset.pop()

        if closeno < openno:
            subset.append(")")
            backtracking(openno, closeno + 1)
            subset.pop()

    backtracking(0, 0)
    return res


print(generateParenthesis(3))
