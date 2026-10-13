class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)

        max = 1
        count = 1
        for index in range(len(nums) - 1):
            if nums[index+1] - nums[index] == 1:
                count += 1
            elif nums[index+1] != nums[index]:
                count = 1
            if count > max:
                max = count
        return max
