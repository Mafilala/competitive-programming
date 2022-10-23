class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        nums.sort()
        ans = [0] * len(temp)
        for i in range(len(nums)):
            index = nums.index(temp[i])
            ans[i] = index
        return ans
        
