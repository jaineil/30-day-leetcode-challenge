class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return(True)
        
        low = 0
        high = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == '(':
                low += 1
                high +=1 
            
            elif s[i] == ')':
                if low > 0:
                    low -= 1
                high -= 1
                
            else:
                if low > 0:
                    low -= 1
                high += 1
            
            if high < 0:
                return(False)
        
        return(low == 0)
    