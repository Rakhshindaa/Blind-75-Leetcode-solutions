class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        preprod=1
        for i in range(len(nums)):
            ans[i]=preprod
            preprod=preprod*nums[i]
        postprod=1
        print(ans)
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postprod
            postprod=postprod*nums[i]
        print(ans)
        return ans
        