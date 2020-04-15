class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        result = [1] * n
        
        for i in range(1,n,1):
            result[i] = nums[i-1] * result[i-1]
        
        mul = 1
        for k in range(n-1,-1,-1):
            result[k] *= mul
            mul *= nums[k]
        
        return(result)