from typing import List


class Solution_121:
    '''
    Complexity is O(n) as we iterate over the elements of the list only once.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        min, max = prices[0], prices[0]
        minI, maxI = 0, 0
        mProfit = 0
        #Loop iterates over the prices list except for the first and last elements
        for i, v in enumerate(prices[1:-1]):
            # Tracks minimum value and stores it
            if v < min:
                minI = i + 1
                min = v

            # Tracks maximum value only if the index of max value is higher than min value index
            if minI >= maxI or v > max:
                maxI = i + 1
                max = v

            # print(minI, maxI, max - min)
            if mProfit < max - min:
                mProfit = max - min

        #Comparing to see if there is a desired solution at the last index
        lastComp = (prices[len(prices) - 1] if prices[len(prices) - 1] > max else max) - min

        mProfit = lastComp if lastComp > mProfit else mProfit
        return mProfit

    '''
    Complexity is same as before O(n). However, I have found this code in Leetcode solution.
    
    My initial idea was to slide the indices window to find the best possible min index and max index. However, I got
    wrong answer when I submitted as the algo was assigned a new minimum value if we could find a value which is "more
    minimum". However, we have to maximize the profit. So, if the new minimum value does not give us better profit,
    we don't need the profit generated with new window. However, I have fixed the issue with the logic but the solution
    still approached sliding the window and picking the best profit.
    
    However, I should have come up with a better approach after I have found the logical problem with the code rather
    than continuing with whatever I have written. Even though the complexity is the same, the code was doing unnecessary
    comparisons and having too many lines. After I have seen this code from LeetCode code sample, I figured we really
    don't need to track max here. We can keep tracking min and the maximum profit we could make before reaching another
    min. We choose the highest profit from all those to get similar result. I could have come up with this solution if
    after realising I have understood the code wrong and came up with a algo from scratch. 
    
    I will keep it in mind next time I solve a question.
    '''
    def maxProfit_clean(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price
            if max_profit < (price - min_price):
                max_profit = (price - min_price)
        return max_profit

    '''
    This was a test to see if there is any improvement in this logic where there are two pointers to solve it. Even
    though the complexity is O(n) same as before, it does not perform better than "maxProfit_clean".
    '''
    def maxProfit_test(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r != len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r
            r += 1

        return max_profit


solution = Solution_121()
print(solution.maxProfit([int(v) for v in input()[1:-1].split(',')]))
print(solution.maxProfit_clean([int(v) for v in input()[1:-1].split(',')]))
print(solution.maxProfit_test([int(v) for v in input()[1:-1].split(',')]))
