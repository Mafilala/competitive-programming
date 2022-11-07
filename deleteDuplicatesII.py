def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    li = []
    ans = ListNode()
    ans_ans = ans
    while head:
        li.append(head.val)
        head = head.next
    ctr = Counter(li)
    set_li = sorted(list(set(li)))
    for s in set_li:
        if ctr[s] == 1:
            ans.next = ListNode(s)
            ans = ans.next
    return ans_ans.next
