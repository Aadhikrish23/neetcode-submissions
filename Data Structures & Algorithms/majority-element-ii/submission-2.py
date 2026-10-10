class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count =Counter(nums)
        ans=set()
        for n in nums:
            if count[n] > (len(nums)//3):
                ans.add(n)

        return list(ans)


        