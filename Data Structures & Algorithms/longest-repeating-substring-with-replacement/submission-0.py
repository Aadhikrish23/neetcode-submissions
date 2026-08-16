class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        start =0
        end=0
        
        max_freq=0  
        max_val = 0

        freq=defaultdict(int)

        while end<len(s):
            freq[s[end]]+=1

            max_freq = max(max_freq,freq[s[end]])

            if (end-start+1)-max_freq>k:
                freq[s[start]]-=1
                start +=1
            
            max_val = max(max_val,(end-start+1))
            end+=1
        return max_val