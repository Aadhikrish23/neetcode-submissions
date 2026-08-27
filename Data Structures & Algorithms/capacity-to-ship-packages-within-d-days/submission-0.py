class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        start = max(weights)
        end =sum(weights)
        ans = end

        while start <= end:
            mid = start + (end-start)//2

            curr_day = 1
            curr_weight = 0

            for w in weights:
                if curr_weight+w >mid:
                    curr_day+=1
                    curr_weight=0
                curr_weight+=w

            if curr_day<=days:
                ans =mid
                end =mid-1
            else:
                start = mid+1
        return ans
                
        