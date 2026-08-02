class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        res = [0] * len(temperatures)
        
        # print(res)
        stack = []
        
        for i in range(len(temperatures)):
            while(len(stack)!=0 and temperatures[i] > temperatures[stack[-1]]):
                index = stack.pop()
                diff = i - index
                res[index] = diff
            
            stack.append(i)
        
        return res