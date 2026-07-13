import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = s.replace(" ", '')
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        left_pointer = 0
        right_pointer = len(s)-1
        while(left_pointer < right_pointer):
            if(65 > ord(s[left_pointer]) > 90 or 48 > ord(s[left_pointer]) > 57 or
            97 > ord(s[left_pointer]) > 122):
                left_pointer +=1
            if(65 > ord(s[left_pointer]) > 90 or 48 > ord(s[left_pointer]) > 57 or
            97 > ord(s[left_pointer]) > 122):
                right_pointer -=1
            if(s[left_pointer] != s[right_pointer]):
                return False
            else:
                left_pointer +=1
                right_pointer -=1
        
        return True