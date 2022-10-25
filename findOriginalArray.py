    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        if changed.count(0) % 2 != 0:
            return []
        ans = []
        counter = Counter(changed)
        changed.sort()
        for num in changed:
            if num == 0 and counter[num]:
                n = counter[num] // 2
                ans.extend([0] * n)
                counter[num] = 0 
            else:
                if counter[num] and counter[num * 2]:
                    counter[num] -= 1
                    counter[num * 2] -= 1
                    ans.append(num)
        if len(ans) != len(changed) / 2:
            return []
        return ans
