def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i, j = 0, 0
    for _ in range(len(pushed)):
        letter = popped[j]
        while i <= pushed.index(letter):
            stack.append(pushed[i])
            i += 1
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        if len(stack) == 0 and j == len(pushed):
            return True
    return False
