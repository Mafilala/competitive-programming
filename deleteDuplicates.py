def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    ans = ListNode(head.val)
    ret = ans
    dup = head.val
    head = head.next
    while head:
        while head and head.val == dup:
            head = head.next
        if head:
            ans.next = ListNode(head.val)
            dup = head.val
            head = head.next
            ans = ans.next
    return ret
