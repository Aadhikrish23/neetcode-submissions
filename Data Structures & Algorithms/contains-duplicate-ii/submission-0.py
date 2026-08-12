class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        seen[nums[0]]=0

        for i in range(1,len(nums)):
            if nums[i] in seen:
                if i-seen[nums[i]] <=k:
                    return True
            
            seen[nums[i]]=i
        return False


        