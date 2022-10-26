class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        i = -2
        ans = 0
        while n > 0:
            ans += piles[i]
            i -= 2
            n -= 1
        return ans
