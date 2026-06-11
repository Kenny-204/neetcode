def letterCombinations(digits):
    if digits == "":
        return []
    res = []

    hashmap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    curr = []

    def backtracking(i):
        if i == len(digits):
            res.append("".join(curr))
            return

        for character in hashmap[digits[i]]:
            curr.append(character)
            backtracking(i + 1)
            curr.pop()

    backtracking(0)
    return res


print(letterCombinations("23"))
