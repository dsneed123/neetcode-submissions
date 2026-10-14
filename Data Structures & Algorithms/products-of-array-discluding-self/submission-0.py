class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        final = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            final[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1,-1):
            final[i] *= postfix
            postfix *= nums[i]
        

        return final
        
        