class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
       
        maxi = max(cntr.values())
      
        return next(x for x in cntr if cntr[x] == maxi)
            
            