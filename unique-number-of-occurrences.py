class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=[]
        count=Counter(arr)
        for i in count.values():
            if i in d:
                return False
            else:
                d.append(i)
        return True

