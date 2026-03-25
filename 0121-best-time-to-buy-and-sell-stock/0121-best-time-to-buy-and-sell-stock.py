class Solution(object):
    def maxProfit(self, prices):
        l, price, max_price = 0, 0, 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            price = prices[r] - prices[l]
            if price > max_price:
                max_price = price

        return max_price
        