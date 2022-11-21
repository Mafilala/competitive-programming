def partitionLabels(self, s: str) -> List[int]:
    ans = []
    part = 0
    end = 0
    hash_map = dict()
    for st in set(s):
        l = s.rfind(st)
        hash_map[st] = l
    for st in s:
        if hash_map[st] > end:
            end = hash_map[st]
        part += 1
        if end + 1 == part + sum(ans):
            ans.append(part)
            part = 0
    return ans
