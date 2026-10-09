class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        seen = Counter(nums)

        max_counts = sorted(seen, key=seen.get, reverse=True)

        return max_counts[:k]