class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = 0
        for i in range(3):
            for j in range(tracker, len(nums)):
                if nums[j] == i:
                    nums[tracker], nums[j] = nums[j], nums[tracker]
                    tracker += 1
                    
                
                    
