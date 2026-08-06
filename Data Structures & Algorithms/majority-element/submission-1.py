class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        seen = Counter(nums)
        return max(seen, key=seen.get)
        