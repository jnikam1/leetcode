class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2[:n]
        nums1.sort()
        # for i in range (m):
        #     nums1.pop()
        # for j in nums2:    
        #     nums1.append(j)
        # nums1.sort()