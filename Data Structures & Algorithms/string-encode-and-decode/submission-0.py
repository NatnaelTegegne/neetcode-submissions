class Solution:

    def encode(self, strs: list[str]) -> str:
        modified_words = [f'{len(word)}#{word}' for word in strs]

        encodedStr = "".join(modified_words)
        return encodedStr

    def decode(self, s: str) -> list[str]:
        list_of_words = []
        pointer = 0
        i = 0

        while(pointer < len(s)):
            if s[i] != "#":
                i +=1
                continue
            else:
                num = s[pointer:i] #the number infront of the delimeter
                num_int = int(num)
                list_of_words.append(s[i+1:num_int+i+1]) #start at the letter next to #
                pointer = num_int+i+1
                i = pointer
        
        return list_of_words