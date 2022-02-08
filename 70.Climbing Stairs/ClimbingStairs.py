class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        
        count=0;
        prev1 = 1
        prev2 = 2
        for i in range (2,n):
            count = prev1 + prev2
            prev1 = prev2
            prev2 = count
        return count
            
        