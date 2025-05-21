class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=sum(nums[:k])
        maxavg=total/k
        for i in range(len(nums)-k):
            total=total-nums[i]
            total=total+nums[i+k]
            maxavg=max(maxavg,total/k)
        return maxavg