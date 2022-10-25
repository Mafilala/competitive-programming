def maxFrequency(self, nums: List[int], k: int) -> int:
    nums.sort()
    total, max_freq = 0, 0
    l, r = 0, 0
    while r < len(nums):
        total += nums[r]
        while (r - l + 1) * nums[r] > total + k:
            total -= nums[l]
            l += 1
        max_freq = max(max_freq, r - l + 1)
        r += 1
    return max_freq
