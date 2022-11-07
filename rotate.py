def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0:
        return
    n = len(nums)
    limit = math.ceil(k / n)
    k = k - (limit - 1) * n
    temp = nums[n - k: n] + nums[:n - k]
    nums[:] = temp
