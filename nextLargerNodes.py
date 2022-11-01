def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    stack = []
    temp_list = []
    while head:
        temp_list.append(head.val)
        head = head.next
    ans = [0] * len(temp_list)
    for i, val in enumerate(temp_list):
        while stack and val > temp_list[stack[-1]]:
            ans[stack.pop()] = val
        stack.append(i)
    return ans
