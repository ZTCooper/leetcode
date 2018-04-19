class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProf, minPrice = 0, float('inf')
        for price in prices:
            minPrice = min(price, minPrice)
            maxProf = max(price - minPrice, maxProf)
        return maxProf
