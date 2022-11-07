def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    l, r = 0, 1
    mini = float('inf')
    total = nums[0]
    flag = False
    while l < r and r <= len(nums):
        if total >= target:
            mini = min(mini, r - l)
            total -= nums[l]
            l += 1
            flag = True
        else:
            if r < len(nums):
                total += nums[r]
            r += 1
    return mini if flag else 0
