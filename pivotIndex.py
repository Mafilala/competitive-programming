def pivotIndex(self, nums: List[int]) -> int:
    sums = [0] * len(nums)
    cum = 0
    for i in range(len(nums)):
        cum += nums[i]
        sums[i] = cum
    for i in range(len(nums)):
        if sums[i] - nums[i] == cum - sums[i]:
            return i
    return -1
