def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for n in nums1:
        appended = False
        start = nums2.index(n)
        temp_arr = nums2[start: ]
        for nn in temp_arr:
            if nn > n:
                ans.append(nn)
                appended = True
                break
        if not appended:
            ans.append(-1)
    return ans
