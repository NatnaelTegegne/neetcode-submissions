class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ('-', '+', '/', '*'):
                a = stack.pop()
                b = stack.pop()
                if(token == '-'):
                    res = b - a
                    stack.append(res)
                elif(token == '*'):
                    res = a * b
                    stack.append(res)
                elif(token == '/'):
                    res = int(b / a)
                    stack.append(res)
                else:
                    res = a + b
                    stack.append(res)
            else:
                stack.append(int(token))
            
        return stack.pop()