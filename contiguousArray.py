class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        net = 0
        max = 0

        for i, x in enumerate(nums):
            if x == 1:
                net += 1
            else:
                net -= 1

            if net in dic:
               l = i - dic[net]
               if l > max:
                   max = l
            else:
                dic[net] = i
                
        return max