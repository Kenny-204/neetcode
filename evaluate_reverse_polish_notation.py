tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]


def evalRPN(tokens):
    def is_numeric_string(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    stack = []
    for token in tokens:
        if is_numeric_string(token):
            stack.append(token)
        else:
            first = stack.pop()
            second = stack.pop()
            if token == "/":
                stack.append(str(int(float(second) / float(first))))
            else:
                res = eval(second + token + first)
                stack.append(str(res))
    return round(float(stack[0]))


print(evalRPN(tokens))
