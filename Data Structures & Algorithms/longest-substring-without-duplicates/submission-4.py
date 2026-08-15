class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        b=0
        e=0
        seen=set()
        max_so_far=0
        while e <=len(s)-1:
            while s[e] in seen:
                seen.remove(s[b])
                b+=1
            seen.add(s[e])
            e+=1
            max_so_far=max(max_so_far,len(seen))

        return max_so_far
            
