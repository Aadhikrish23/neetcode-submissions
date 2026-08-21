class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        start =1
        end =max(piles)
        ans =end
        while start <=end:
            mid =start+(end-start)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            
            if total <=h:
                ans = mid
                end = mid-1
            else:
                start=mid+1
            
        return ans