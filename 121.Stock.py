def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0
    max_profit = 0
    min = 9999

    for price in prices:
        if price < min:
            min = price
        profit = price - min
        if(profit > max_profit):
            max_profit = profit
    return max_profit

prices = [7,6,4,3,1]
maxProfit(prices)

# iterate through the array
# store the max profit; find the profit for each iteration
# if the profit > stored max, replace max_profit
# return max_profit