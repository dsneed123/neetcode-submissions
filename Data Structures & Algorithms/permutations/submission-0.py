class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0: #base case
            return [[]]

        perms = self.permute(nums[1:]) #compute every permutation 

        res = []

        for p in perms:
            for i in range(len(p) + 1): #add permutations back by 1 int
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res