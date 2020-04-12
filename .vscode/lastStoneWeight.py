class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       
    # loop iterates until two stones are left and either both are killed because they are equal making our solution zero or one of the stone kills another and their difference is our result
        while(len(stones)>1): 
            
            stones.sort() 
            # key idea is to sort the stones in each iteration so as to easily pick the 2 heaviest stones
        
            x = stones[-1] # taking the heaviest stone
            y = stones[-2] # taking the second heaviest stone
        
            stones.remove(x) # we have to remove those weights irrespective of whether they are same
            stones.remove(y)
        
            if x > y:
                stones.append(x-y)
            elif x < y:
                stones.append(y-x)
        
        if len(stones) == 1:
            return(stones[0])
        elif len(stones) == 0:
            return 0
        
        
        
        
        
        