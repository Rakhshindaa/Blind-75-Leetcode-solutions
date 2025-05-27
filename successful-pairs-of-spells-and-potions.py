class Solution:
    def bsearch(self,spell:int,potions:list[int],success:int) -> int:
        l=0
        r=len(potions)-1
        while l<=r:
            mid=(l+r)//2
            if spell*potions[mid]>=success:
                r=mid-1
            else:
                l=mid+1
        return l
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        potions.sort()
        for sp in spells:
            ans.append(len(potions)- self.bsearch(sp,potions,success))
        return ans