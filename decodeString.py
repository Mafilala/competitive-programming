def decodeString(self, s: str) -> str:
    stack = []
    store = ""
    num = ""
    for i in range(len(s)):
        char = s[i]
        if char == "]":
            while stack[-1] != "[":
                store = stack.pop() + store
            stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            if num:
                store *= int(num)
                num = ""
            stack.append(store)
            store = ""
        else:
            stack.append(char)
    return "".join(stack)
