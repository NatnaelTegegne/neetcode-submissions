class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        empty = []
        for i in range(len(nums)):
            if target - nums[i] not in numsDic.values():
                numsDic[i] = nums[i]
            else:
                indexes = [nums.index(target - nums[i]), i]
                return indexes
        
         # numsDic = {index: item for index, item in enumerate(nums)}

        
        # for k, v in numsDic.items():
        #     if (target - v in numsDic.values()):
        #         indexes = [k, list(key for key, value in numsDic.items() if value == target - v)]
        #         return indexes
        
        return empty