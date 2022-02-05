class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        list1 = []
        for i in range(len(nums)):
            list1.append(nums[i])
            if nums[i]==target:
                return i
            else:
                list1.append(target)
        test_list = list(set(list1))
        test_list.sort()
        return test_list.index(target)
            
            