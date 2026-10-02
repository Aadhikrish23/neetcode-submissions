class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_i =Counter(s)
        seen_j =Counter(t)


     
        if seen_i == seen_j:
            return True
        else:
            return False