class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        i = 1
        ans = []
        merged = intervals[0]
        while i < len(intervals):
            if intervals[i][0] <= merged[1]:
                merged[1] = max(merged[1], intervals[i][1])
                i += 1
                if i == len(intervals):
                    ans.append(merged)
            else:
                ans.append(merged)
                merged = intervals[i]
                i += 1
                if i == len(intervals):
                    ans.append(merged)
        return ans
                
            
        
        
