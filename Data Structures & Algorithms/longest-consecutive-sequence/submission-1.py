class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_so_far = 0 
        for n in nums:
            if n-1 not in numset:
                length = 0
                while (n+length) in numset:
                    length+=1
                
                max_so_far = max(length,max_so_far)

        return max_so_far

        