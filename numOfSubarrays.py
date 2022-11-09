def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    l = res = 0
    r = l + k
    su = sum(arr[l:r])
    cmps = k * threshold
    while r <= len(arr):
        if su >= cmps:
            res += 1
        su -= arr[l]
        l += 1
        if r < len(arr):
            su += arr[r]
        r += 1
    return res
