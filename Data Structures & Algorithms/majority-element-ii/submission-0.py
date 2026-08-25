class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        import math
        seen = Counter(nums)
        ans = []

        for num in seen:
            mincount = math.floor(len(nums)/3)
            if seen[num]>mincount:
                ans.append(num)
        
        return ans