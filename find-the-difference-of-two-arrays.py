class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=set(nums1)
        l2=set(nums2)
        ans1=list(l1-l2)
        ans2=list(l2-l1)
        return [ans1,ans2]