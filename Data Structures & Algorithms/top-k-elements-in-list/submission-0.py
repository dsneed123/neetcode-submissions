class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_dict = sorted(count, key=count.get, reverse=True)
        biggest = []
        for i in range(k):
            biggest.append(sorted_dict[i])

        return biggest
        