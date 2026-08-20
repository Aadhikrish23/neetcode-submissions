class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x//2

        ans = 0

        if x < 2:
            return x

        while start<=end:
            mid = start+(end-start)//2

            if mid <= x//mid:
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans
