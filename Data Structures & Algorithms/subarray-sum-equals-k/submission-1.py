class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res =0
        prefixsum={0:1}
        current=0

        for num in nums:
            current+=num
            diff = current-k
            res += prefixsum.get(diff,0)
            prefixsum[current ]=1+prefixsum.get(current,0)

        return res
