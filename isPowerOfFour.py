def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
        return False
    if n % 4 != 0 and n != 1:
        return False
    if n == 1:
        return True
    return self.isPowerOfFour(n // 4)
