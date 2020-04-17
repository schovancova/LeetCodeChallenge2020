class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        find_min = True
        account = 0
        leng = len(prices)
        for x in range(0, leng):
            if x == leng - 1:
                if not find_min:
                    account += prices[x]
                break
            if find_min:
                if prices[x] < prices[x + 1]:
                    account -= prices[x]
                    find_min = False
            else:
                if prices[x] > prices[x + 1]:
                    account += prices[x]
                    find_min = True
        return account
