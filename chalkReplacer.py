def chalkReplacer(self, chalk: List[int], k: int) -> int:
    n = len(chalk)
    tot = sum(chalk)
    round = math.ceil(k / tot)
    k = k - (round - 1) * tot
    cum = 0
    for i in range(n):
        cum += chalk[i]
        if cum > k:
            return i
    return 0
