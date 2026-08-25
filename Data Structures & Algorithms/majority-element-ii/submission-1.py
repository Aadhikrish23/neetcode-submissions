class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        canditate1=None
        canditate2=None
        count1=0
        count2=0
        ans=[]

        for num in nums:
            if num==canditate1:
                count1+=1
            elif num==canditate2:
                count2+=1
            elif count1 ==0:
                canditate1 = num
                count1+=1
            elif count2==0:
                canditate2 = num
                count2+=1
            else:
                count1-=1
                count2-=1
            
        count1=0
        count2=0
        for num in nums:
            if num==canditate1:
                count1+=1
            elif num==canditate2:
                count2+=1
        
        if count1>len(nums)//3:
            ans.append(canditate1)
        if count2>len(nums)//3:
            ans.append(canditate2)

        return ans
