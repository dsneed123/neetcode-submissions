class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        pairs = {")" : "(", "]": "[", "}" : "{"}
        stack = []
        
        for char in s:
            if char not in pairs:
                stack.append(char)
            
            else:
                #if stack is empty or top does in the dict
                if not stack or stack[-1] != pairs[char]: 
                    return False
                stack.pop()


        return not stack #if the stack is empty itll return True 

        