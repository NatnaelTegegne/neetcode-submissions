class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(numbers)):
            n = target - numbers[i]
            l = i + 1
            r = len(numbers) - 1
            while(l<= r):
                if(numbers[l] == n):
                    output.append(i+1)
                    output.append(l+1)
                    return output
                elif(numbers[r] == n):
                    output.append(i+1)
                    output.append(r+1)
                    return output
                else:
                    l += 1
                    r -= 1
        
        return output