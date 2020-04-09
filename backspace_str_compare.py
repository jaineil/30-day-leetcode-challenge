class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        s = list(S)
        t = list(T)
        
        stack1 = []
        
        for i in range(len(s)):
            if s[i] != '#':
                stack1.append(S[i])
            elif s[i] == '#' and len(stack1) != 0:
                stack1.pop()
            
        stack2 = []
        
        for i in range(len(t)):
            if t[i] != '#':
                stack2.append(t[i])
            if t[i] == '#' and len(stack2) != 0:
                stack2.pop()
        
        if stack1 == stack2:
            return(True)
        else: 
            return(False)