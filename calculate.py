def calculate(self, s: str) -> int:
    stack = []
    cur = 0
    operators = ["+", "-", "/", "*"]
    sign = "+"
    s = s.replace(" ", "")
    for nu in s + "M":
        if nu.isdigit():
            cur = (cur * 10) + int(nu)
        else:
            if sign == "+":
                stack.append(cur)
            elif sign == "-":
                stack.append(-cur)
            elif sign == "*":
                stack.append(stack.pop() * cur)
            elif sign == "/":
                stack.append(int(stack.pop() / cur))
            sign = nu
            cur = 0
    return sum(stack)
