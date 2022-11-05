def lengthOfLongestSubstring(self, s: str) -> int:
    i = 0
    j = 0
    maximum = 0
    uniqueSet = []
    while i < len(s):
        while s[i] in uniqueSet:
            uniqueSet.remove(s[j])
            j += 1
        uniqueSet.append(s[i])
        i += 1
        maximum = max(maximum, i - j)

    return maximum
