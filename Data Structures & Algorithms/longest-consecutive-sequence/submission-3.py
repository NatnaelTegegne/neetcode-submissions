class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for i in range(len(nums)):
            if(nums[i] - 1 not in nums_set): #means this is a start of a streak
                current_num = nums[i]
                current_streak = 1
                is_seq = True
                while(is_seq):
                    if(current_num + 1 in nums_set):
                        current_streak +=1
                        current_num +=1
                    else:
                        is_seq = False
                if(current_streak > longest_streak):
                    longest_streak = current_streak
        

        return longest_streak