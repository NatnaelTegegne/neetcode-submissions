import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        return heapq.nlargest(k, dic, key=dic.get)
