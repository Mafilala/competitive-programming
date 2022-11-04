def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    new_head = ListNode()
    dummy = new_head
    while head:
        if not head.next:
            new_head.next = ListNode(head.val)
            head = head.next
        else:
            new_head.next = ListNode(head.next.val)
            new_head = new_head.next
            new_head.next = ListNode(head.val)
            head = head.next.next
            new_head = new_head.next
    return dummy.next
