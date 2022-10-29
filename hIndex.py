def hIndex(self, citations: List[int]) -> int:
    ctr = Counter(citations)
    ord_ctr = [[v, ctr[v]] for v in ctr]
    ord_ctr.sort(reverse=True)
    behind = 0
    max_ = ord_ctr[0][0]
    while max_ > 0:
        if max_ in ctr.keys():
            behind += ctr[max_]

        if behind >= max_:
            return max_
        max_ -= 1
    return 0 if max(citations) == 0 else 1
