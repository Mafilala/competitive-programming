    def minSetSize(self, arr: List[int]) -> int:
        half_l = len(arr) // 2
        c = Counter(arr)
        idx = 0
        ans = 0
        for val, ct in c.most_common():
            ans += 1
            idx += ct
            if idx >= half_l:
                break
        return ans
