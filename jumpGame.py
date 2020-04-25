# I hate this question. It looks like Graph Search. It looks like Backtracking. 
# And then...the answer is just reverse linear sweep. Damn you Occam's razor.
# Best explanation for the problem: https://www.youtube.com/watch?v=Zb4eRjuPHbM

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndexPosition = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if (i + nums[i]) >= lastGoodIndexPosition:
                lastGoodIndexPosition = i
                
        return lastGoodIndexPosition == 0