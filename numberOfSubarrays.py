def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i] = 0
        else:
            nums[i] = 1
    cum = 0
    res = 0
    hash_map = {0:1}
    for j in range(len(nums)):
        cum += nums[j]
        if cum - k in hash_map:
            res += hash_map[cum - k]
        hash_map[cum] = hash_map.get(cum, 0) + 1
    return res
