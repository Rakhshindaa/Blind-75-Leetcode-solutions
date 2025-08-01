class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        left,count=0,0
        for i in range(n):
            if nums[i]==0:
                count+=1
            if count>1:
                if nums[left]==0:
                    count-=1
                left+=1
        return n-left-1
        