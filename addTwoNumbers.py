def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ans = ListNode()
    rep = ans
    carry = 0
    fv = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        fv = val1 + val2 + carry
        carry = fv // 10
        fv = fv if fv < 10 else fv % 10
        ans.next = ListNode(fv)
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        ans = ans.next
    return rep.next
