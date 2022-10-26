    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = []
        for val, ct in c.most_common(k):
            ans.append(val)
        return ans
        
