class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr,L,R,M):
            i,j,k = L,0,0
            Left = arr[L:M+1]
            Right = arr[M+1:R+1]

            while j<len(Left) and k< len(Right):
                if Left[j] <=Right[k]:
                    arr[i]=Left[j]
                    j+=1
                else:
                    arr[i] = Right[k]
                    k+=1
                i+=1
            while j<len(Left):
                arr[i]=Left[j]
                j+=1
                i+=1

            while k<len(Right):
                arr[i]=Right[k]
                k+=1
                i+=1
           

        def mergesort(arr,l,r):
            if l == r:
                return arr
            mid = l+(r-l)//2
            mergesort(arr,l,mid)
            mergesort(arr,mid+1,r)

            merge(arr,l,r,mid)
            return arr
        
        return mergesort(nums,0,len(nums)-1)