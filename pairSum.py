def pairSum(self, head: Optional[ListNode]) -> int:
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    for i in range(len(stack) // 2):
        stack[i] += stack.pop()
    return max(stack)
