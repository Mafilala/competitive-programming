def compress(self, chars: List[str]) -> int:
    i = 0
    res = []
    while i < len(chars):
        j = i
        cnt = 0
        while j < len(chars) and chars[j] == chars[i]:
            cnt += 1
            j += 1
        if cnt == 1:
            res.append(chars[i])
        else:
            cnt = list(str(cnt))
            res.append(chars[i])
            res.extend(cnt)
        i = j
    n = len(res)
    chars[:n] = res
    chars[n:] = []
    return n
