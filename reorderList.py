def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    dummy = head
    track = head
    temp_list = []
    while track:
        temp_list.append(track.val)
        track = track.next
    half = (len(temp_list) + 1) // 2
    l1 = temp_list[:half]
    l2 = reversed(temp_list[half:])
    temp_list[::2] = l1
    temp_list[1::2] = l2
    i = 0
    while head:
        head.val = temp_list[i]
        head = head.next
        i += 1
    return dummy
