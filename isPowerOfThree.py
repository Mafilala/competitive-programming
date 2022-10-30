def isPowerOfThree(self, n: int) -> bool:
    if n == 0 or n == -1:
        return False
    ans = math.log(abs(n), 3)
    ans = math.ceil(ans)
    return math.pow(3, ans) == n
