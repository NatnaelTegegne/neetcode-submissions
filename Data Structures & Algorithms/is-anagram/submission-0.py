from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        hashS = dict(Counter(s))
        hashT = dict(Counter(t))

        for key, value in hashS.items():
            if(hashS[key] != hashT.get(key)):
                return False
        
        return True
        
        