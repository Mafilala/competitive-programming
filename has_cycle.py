def has_cycle(head):
    stack = []
    while head:
        if str(head.data)[-1] == "m":
            return 1
        head.data = str(head.data) + 'm'
        head = head.next
    return 0
