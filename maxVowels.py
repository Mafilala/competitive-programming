def maxVowels(self, s: str, k: int) -> int:
    l, v_count, res = 0, 0, 0
    vowels = "aeiou"
    for r in range(len(s)):
        if s[r] in vowels:
            v_count += 1
        if (r - l + 1) == k:
            res = max(res, v_count)
            if s[l] in vowels:
                v_count -= 1
            l += 1
    return res
