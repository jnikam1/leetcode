class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        if not nums:
            return 0
        for x in range (len(nums)):
            if (val!=nums[x]):
                nums[index]=nums[x]
                index +=1

        return index