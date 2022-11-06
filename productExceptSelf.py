def productExceptSelf(self, nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    ans[0] = 1
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
    psf = 1
    for j in range(len(nums) - 1, -1, -1):
        ans[j] *= psf
        psf *= nums[j]
    return ans
