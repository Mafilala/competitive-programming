class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            
