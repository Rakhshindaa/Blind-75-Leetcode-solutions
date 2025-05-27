class RecentCounter:

    def __init__(self):
        self.req=[]
        self.start=0
    def ping(self, t: int) -> int:
        self.req.append(t)
        while self.req[self.start]<t-3000:
            self.start+=1
        return len(self.req)-self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)