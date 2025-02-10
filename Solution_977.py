import math
from typing import List


class Solution_977:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        output = []
        while l != r:
            if abs(nums[l]) >= abs(nums[r]):
                output.append(math.pow(nums[l], 2))
                l += 1
            else:
                output.append(math.pow(nums[r], 2))
                r -= 1

        # To insert the squared value of the index where l=r
        output.append(math.pow(nums[l], 2))

        return [int(v) for v in output[::-1]]

    '''
    The solution I have generated has a time complexity of O(n). The solution below has a time complexity of O(nlogn).
    However, the algorithm outperforms my solution in terms of real-life runtime as num*num is faster than math.pow();
    all the comparisons and extra lines that executed; and, the sorted() function being very efficient. Good learning.
    '''
    def sortedSquares_improved(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)


solution = Solution_977()
print(solution.sortedSquares([int(v) for v in input()[1:-1].split(",")]))
print(solution.sortedSquares_improved([int(v) for v in input()[1:-1].split(",")]))
