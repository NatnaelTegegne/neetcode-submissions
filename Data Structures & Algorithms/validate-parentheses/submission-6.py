class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if(s == ""):
            return False
        
        
        for i in s:
            if(i == "(" or i == "[" or i == "{"):
                stack.append(i)
            else:
                if(len(stack)==0 and (i == ")" or i == "]" or i == "}")):
                    return False
                top = stack.pop()
                if(top == '{' and i == '}' or top == '(' and i == ')'
                   or top == '[' and i == ']'):
                    continue
                else:
                    return False
                
        if(len(stack) == 0):
            return True
        else:
            return False