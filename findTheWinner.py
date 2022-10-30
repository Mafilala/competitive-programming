def findTheWinner(self, n: int, k: int) -> int:
    def recurse(li, pt):
        print(li)
        if len(li) == 1:
            return li.pop()
        else:
            new_pt = (pt + k) % len(li)
            num = li[new_pt]
            li.remove(num)
            return recurse(li, new_pt - 1)
    inp = [nm for nm in range(1, n + 1)]
    ans = recurse(inp, -1)
    return ans
