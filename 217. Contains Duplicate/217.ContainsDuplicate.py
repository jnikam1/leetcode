class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (len(nums)):
            if (i+1<len(nums) and nums[i]==nums[i+1]):
                return True
            else:
                continue
        return False