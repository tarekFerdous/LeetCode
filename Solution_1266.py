import re
from typing import List


class Solution_1266:
    '''
    The solution here is pretty straight-forward. When we travel one point to another we try to cover the distance by 1
    unit each time. This could be done vertically (y-axis), horizontally (x-axis) or, diagonally. So, one solution can
    be to sum all the maximum distance covered in either of the direction. This trend can be found in the example. There,
    we can see that the movement is done by adding/substracting from x and y axis in each step while we can and then
    adding 1 more unit to reach the actual destination if the actual destination is not positioned diaginally from the
    last position in the path. We do that to all the pairs in the same sequence as the given 2D array and we get our
    solution.
    '''
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i in range(1, len(points)):
            distance += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))

        return distance


solution = Solution_1266()
'''
List comprehension: I have tried to learn more about list comprehension. This below is a one liner for taking input as
it is from leetcode (only for this specific problem). I have tried to find all the strings that matches with a pattern
and turn them into a list in the outer []. Further process was done on each specific values of the generated list. Each
value were split and turned into an integer in the inner [].

Regex: I have also started revising regex, a very powerful tool to match pattern. The https://pythex.org/ was very
helpful. The cheatsheet from this website was short and precise. The interesting part is you can visualize matched 
substrings being highlighted in the text as you write the regex.
'''
points = [[int(z) for z in v.split(',')] for v in re.findall("-?\d+,-?\d+", input())]
print(solution.minTimeToVisitAllPoints(points))
