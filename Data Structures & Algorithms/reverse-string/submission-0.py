class Solution:
    def reverseString(self, s: List[str]) -> None:
       
        b = 0
        e =(len(s)-1)
        while b<e:
            s[b],s[e]=s[e],s[b]
            b+=1
            e-=1