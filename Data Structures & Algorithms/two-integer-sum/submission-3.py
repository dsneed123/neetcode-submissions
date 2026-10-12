class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set(nums)

        for index,num in enumerate(nums):
            sub_target = target - num 
            if sub_target in num_set:
                j = nums.index(sub_target)
                if j != index:
                    return sorted([index, j])