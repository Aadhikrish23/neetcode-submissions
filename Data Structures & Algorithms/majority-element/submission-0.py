class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        seen = Counter(nums)

        max_count = max(seen.values())

        max_val = {value: key for key, value in seen.items()}

        return max_val[max_count]
        