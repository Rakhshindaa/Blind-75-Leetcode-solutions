class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        total=sum(nums)
        for i in range(len(nums)):
            if leftsum == total-leftsum-nums[i]:
                return i
            leftsum=leftsum+nums[i]
        return -1
