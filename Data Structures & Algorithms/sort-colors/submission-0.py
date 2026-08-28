class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = [0]*len(nums)

        def mergesort(left,right):
            if left >= right:
                return
            
            mid = (left+right)//2

            mergesort(left,mid)
            mergesort(mid+1,right)

            i=left
            j=mid+1
            k= left

            while i <= mid and j<=right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1

                k += 1
            
            while i<=mid:
                temp[k] = nums[i]
                i += 1
                k+=1
            while j<= right:
                temp[k]=nums[j]
                j+=1
                k+=1
            
            for i in range(left,right+1):
                nums[i]=temp[i]

        mergesort(0,len(nums)-1)

            




     
