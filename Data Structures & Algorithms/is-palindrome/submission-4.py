import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()

        left_pointer = 0
        right_pointer = len(s)-1
        while(left_pointer < right_pointer):
            if((ord(s[left_pointer]) not in range(48, 58))
             and (ord(s[left_pointer]) not in range(97,123))):
                left_pointer +=1
                #continue to make sure the current increment doesn't swap the pointers past each other
                continue
            if((ord(s[right_pointer]) not in range(48, 58))
             and (ord(s[right_pointer]) not in range(97,123))):
                right_pointer -=1
                continue
            if(s[left_pointer] != s[right_pointer]):
                return False
            else:
                left_pointer +=1
                right_pointer -=1
        
        return True