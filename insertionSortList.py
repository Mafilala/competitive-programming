def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node_list = []
    while head:
        node_list.append(head.val)
        head = head.next

    for i in range(1, len(node_list)):
        j = i - 1
        key = node_list[i]
        while j >= 0 and key < node_list[j]:
            node_list[j + 1] = node_list[j]
            j -= 1
        node_list[j + 1] = key

    ls = ListNode()
    dummy = ls

    for val in node_list:
        ls.next = ListNode(val)
        ls = ls.next
    return dummy.next
