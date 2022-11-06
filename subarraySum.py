def subarraySum(self, nums: List[int], k: int) -> int:
    hash_map = {0:1}
    sum = 0
    res = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in hash_map:
            res += hash_map[sum - k]
        hash_map[sum] = 1 + hash_map.get(sum, 0)
    return res
