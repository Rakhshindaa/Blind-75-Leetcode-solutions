class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandi=max(candies)
        res=[False]*(len(candies))
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxcandi:
                res[i]=True
        return res