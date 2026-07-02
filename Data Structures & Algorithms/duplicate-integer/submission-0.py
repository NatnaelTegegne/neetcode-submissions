class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inList = set()

        for i in nums:
            if(i in inList):
                return True
            inList.add(i)
        
        return False