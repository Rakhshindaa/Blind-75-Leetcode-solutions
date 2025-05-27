class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx=0
        curr=0
        for i in gain:
            curr=curr+i
            maxx=max(maxx,curr)
        return maxx