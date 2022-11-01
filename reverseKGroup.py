def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    stack = []
    count = 0
    ans = ListNode()
    ret = ans
    while head:
        count += 1
        stack.append(head.val)
        head = head.next
    rev_stack = [0] * count
    ini = 0
    fin = k
    while fin <= count:
        rev_stack[ini: fin] = reversed(stack[ini: fin])
        ini = fin
        fin = fin + k
    while ini < count:
        rev_stack[ini] = stack[ini]
        ini += 1
    for ele in rev_stack:
        ans.next = ListNode(ele)
        ans = ans.next
    return ret.next
