    def isValid(self, s: str) -> bool:
        op = ['(', '[', '{']
        cl = [')', ']', '}']
        stack = []
        if s[0] in cl or  s[-1] in op or len(s) % 2 != 0:
            return False
        for ch in s:
            if ch in op:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last = stack[-1]
                if cl.index(ch) != op.index(last):
                    return False
                stack.pop()
        return len(stack) == 0
        
