def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    ans = ListNode()
    dummy = ans
    while list1 or list2:
        if list1 and list2:
            if list1.val < list2.val:
                ans.next = ListNode(list1.val)
                ans = ans.next
                list1 = list1.next
            elif list1.val > list2.val:
                ans.next = ListNode(list2.val)
                ans = ans.next
                list2 = list2.next
            else:
                ans.next = ListNode(list1.val)
                ans = ans.next
                list1 = list1.next
                ans.next = ListNode(list2.val)
                list2 = list2.next
                ans = ans.next
        elif list1:
            while list1:
                ans.next = ListNode(list1.val)
                ans = ans.next
                list1 = list1.next
        else:
            while list2:
                ans.next = ListNode(list2.val)
                ans = ans.next
                list2 = list2.next
    return dummy.next
