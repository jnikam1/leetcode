class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedstring1= sorted(s)
        sortedstring2= sorted(t)
        if (len(s)!=len(t)): return False
        elif (sortedstring1==sortedstring2):
            return True
        return False
        