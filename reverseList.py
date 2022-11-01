def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    ans = ListNode(head.val)
    head = head.next
    while head:
        temp = ListNode(head.val)
        temp.next = ans
        ans = temp
        head = head.next
    return temp
