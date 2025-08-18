class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        buy=float('-inf')
        sell=0
        for p in prices:
            buy=max(buy,sell-p)
            sell=max(sell,buy+p-fee)
        return sell
            