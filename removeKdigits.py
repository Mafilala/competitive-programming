def removeKdigits(self, num: str, k: int) -> str:
    if len(num) <= k:
        return "0"
    stack = []
    stack.append(num[0])
    for i in range(1, len(num)):
        while k and stack and int(stack[-1]) > int(num[i]):
            stack.pop()
            k -= 1
        stack.append(num[i])
    while k:
        stack.pop()
        k -= 1
    return str(int("".join(stack)))
