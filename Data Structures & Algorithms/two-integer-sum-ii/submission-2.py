class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_set = set(numbers)


        for index,nums in enumerate(numbers):
            if target - nums in my_set:
                if numbers.index(target - nums) != index:
                    return sorted([index + 1, numbers.index(target - nums) + 1])
        