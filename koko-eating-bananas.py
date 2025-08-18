class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1 #minimum k value- lower bound
        right=max(piles)  #maximum k value - upper bound
        while left<right:
            mid=(left+right)//2
            t=0
            #calculating total hours
            for p in piles:
                t+=(p+mid-1)//mid
            #if total hours exceed 'h' which means it is invalid to move right to mid
            if t<=h:
                right=mid
            else:
                left=mid+1  #speed is too slow so increment left
        return left #when left==right we found minimum valid speed