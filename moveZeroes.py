class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        z = len(nums)
        for i in range(z):
            if nums[i] != 0:
                nums[count] = nums[i] 
                count += 1
        while count < z:
            nums[count] = 0
            count += 1