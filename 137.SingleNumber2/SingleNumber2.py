class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1= Counter(nums)
        # print (dict1)
        for i,v in dict1.items():
            if (v==1):
                return i
        