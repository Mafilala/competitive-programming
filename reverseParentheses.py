def reverseParentheses(self, s: str) -> str:
    stack = [""]
    for sy in s:
        if sy == "(":
            stack.append('""')
        elif sy == ")":
            temp = stack.pop()[::-1]
            stack[-1] += temp
        else:
            stack[-1] += sy
    return "".join(stack).replace('""', "")
