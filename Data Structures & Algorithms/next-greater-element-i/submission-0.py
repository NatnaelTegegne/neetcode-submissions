class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        res = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i] == nums2[j]):
                    found = nums2[j]
                    while(j < len(nums2)):
                        if(nums2[j] > found):
                            res[i] = nums2[j]
                            break
                        else:
                            j +=1
        
        return res