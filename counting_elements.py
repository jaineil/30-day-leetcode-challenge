''' Given an integer array arr, count element x such that x+1 is also in arr.
If there are duplicates in arr, count them seperately.''' 

class Solution:
    def countElements(self, arr: List[int]) -> int:
        lookup = set(arr)
    
        res = 0
        for j in arr:
            if j+1 in lookup:
                res += 1
        
        return(res)