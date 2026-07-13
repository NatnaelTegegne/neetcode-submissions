from bisect import bisect_left
class Solution:
    def binary_search(self, sorted_list, target):
        index = bisect_left(sorted_list, target)
        
        if index < len(sorted_list) and sorted_list[index] == target:
            return index
        
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(numbers)):
            index = self.binary_search(numbers, target - numbers[i])
            if(index != -1):
                output.append(i+1)
                output.append(index+1)
                break
        
        return output