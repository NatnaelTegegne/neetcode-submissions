class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output, prefix, postfix = [], [], []
        num = 1
        prefix.append(num)
        postfix.append(num)

        for i in range(len(nums)):
            num *= nums[i]
            prefix.append(num)

        #start at the back of the nums array and go to the front multiplying by
        #preceeding number and append it to the postfix array
        num = 1
        for i in range(-1, -len(nums), -1):
            num *= nums[i]
            postfix.append(num)

        #update the postfix array by reversing it so that it is easier to multiply
        #the elements in the prefix array
        postfix = postfix[::-1]

        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])
        return output