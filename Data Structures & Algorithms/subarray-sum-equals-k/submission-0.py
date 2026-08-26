class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        curr = 0
        count = 0
        for num in nums:
            curr+=num

            if (curr-k) in seen:
                count+=seen[curr-k]
            seen[curr]=seen.get(curr,0)+1
        return count