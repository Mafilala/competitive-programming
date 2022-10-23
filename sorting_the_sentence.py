class Solution:
    def sortSentence(self, s: str) -> str:
        new_list = s.split(" ")
        n = len(new_list)
        ans = [None] * n
        for wd in new_list:
            index = int(wd[-1]) - 1
            ans[index] = wd[:-1]
        return " ".join(ans)
            
        
