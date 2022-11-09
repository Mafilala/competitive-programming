def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []
    s_map, p_map = {}, {}
    for i in range(len(p)):
        p_map[p[i]] = 1 + p_map.get(p[i], 0)
        s_map[s[i]] = 1 + s_map.get(s[i], 0)
    ans = [0] if s_map == p_map else []
    l = 0
    for r in range(len(p), len(s)):
        s_map[s[r]] = 1 + s_map.get(s[r], 0)
        s_map[s[l]] -= 1
        if s_map[s[l]] == 0:
            s_map.pop(s[l])
        l += 1
        if s_map == p_map:
            ans.append(l)
    return ans
