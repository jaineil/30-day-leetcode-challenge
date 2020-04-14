class Solution:

#You may notice that left shift cancels the right shift, so count the total and perform the shift once. #Using the single shift logic

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        finalShift = 0
        
        for i in range(len(shift)):
            direction = shift[i][0]
            amount = shift[i][1]
            if direction == 0:
                finalShift -= amount
            else:
                finalShift += amount
                
        l = len(s)
        
        if finalShift < 0:
            #left shift 
            finalShift = abs(finalShift) % l #handles when finalShift > len(s)
            finalFront = s[abs(finalShift):]
            finalBack = s[:abs(finalShift)]
            
        elif finalShift > 0:
            #right shift 
            finalShift = finalShift % l #handles when finalShift > len(s)
            finalFront = s[l-finalShift:]
            finalBack = s[:l-finalShift]
            
        else:
            return s
        
        return(finalFront + finalBack)