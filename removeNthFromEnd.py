def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    length = 0
    temp = head
    ret = head
    prev = None
    while temp:
        length += 1
        temp = temp.next
    length = length - n
    if not length:
        return ret.next
    while length:
        if length == 1:
            prev = head
        head = head.next
        length -= 1
    prev.next = head.next
    return ret 
