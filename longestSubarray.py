def longestSubarray(self, nums: List[int]) -> int:
    ans = sum = l = 0
    for h, num in enumerate(nums):
        sum += num
        if sum < h - l:
            sum -= nums[l]
            l += 1
        ans = max(ans, h - l)
    return ans
