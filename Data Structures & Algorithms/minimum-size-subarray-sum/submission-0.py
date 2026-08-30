class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0

        minval = float("inf")

        curr = 0
        while end<len(nums):
            curr +=nums[end]
            while curr>= target:
                curval = end-start+1
                minval = min(curval,minval)
                curr-=nums[start]
                start+=1
            end+=1

        return 0 if minval==float("inf") else minval