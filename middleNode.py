def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = head
    count = 0
    while head:
        count += 1
        head = head.next
    limit = count // 2
    while limit:
        dummy = dummy.next
        limit -= 1
    return dummy
