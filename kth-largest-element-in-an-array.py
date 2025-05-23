class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=list(sorted(nums,reverse=True))
        return arr[k-1]