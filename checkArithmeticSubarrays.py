    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        def isArth(arr):
            arr.sort()
            const = arr[1] - arr[0]
            if len(arr) <= 2:
                return True
            for i in range(1, len(arr)):
                if arr[i] - arr[i - 1] != const:
                    return False
            return True
        for j in range(len(l)):
            temp_arr = nums[l[j] : r[j] + 1]
            answer.append(isArth(temp_arr))
        return answer
            
