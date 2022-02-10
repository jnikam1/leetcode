class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict1= Counter(nums)
        list1=[]
        for i,v in dict1.items():
            if (v==1):
                list1.append(i)
        return list1