from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1 # using letter 'a' as a relative, place each char in the freq list
            
            #make the key (freq list) immutable and add it to the dic
            dic[tuple(freq)].append(s)
        
        return list(dic.values())