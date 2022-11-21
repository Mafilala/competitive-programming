def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    list_node = []
    while head:
        list_node.append(head.val)
        head = head.next
    list_node.sort()
    res = ListNode()
    ans = res
    for val in list_node:
        res.next = ListNode(val)
        res = res.next
    return ans.next
