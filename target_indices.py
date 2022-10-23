class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        try:
            ans = [nums.index(target)]
        except:
            return []
        i = ans[0]
        while i < n - 1 and nums[i] == nums[i + 1]:
            ans.append(i + 1)
            i += 1
        return ans
