class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        f=float('inf')
        s=float('inf')
        for i in nums:
            if i<=f:
                f=i
            elif i<=s:
                s=i
            else:
                return True
        return False
        