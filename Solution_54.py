import re
from typing import List


class Solution_54:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        tracker = [[0 for z in v] for v in matrix]

        output = []
        i = 1
        while True:
            # left->right
            output.extend(matrix[i - 1][i - 1:len(matrix[i - 1]) - i + 1])
            tracker[i - 1][i - 1:len(matrix[i - 1]) - i + 1] = [1 for v in
                                                                matrix[i - 1][i - 1:len(matrix[i - 1]) - i + 1]]

            if not any(True for lst in tracker if 0 in lst):
                break

            # top->bottom
            for lst in matrix[i:len(matrix) - i]:
                output.append(lst[len(lst) - i])
                tracker[matrix.index(lst)][len(lst) - i] = 1

            if not any(True for lst in tracker if 0 in lst):
                break

            # right<-left
            output.extend(matrix[len(matrix) - i][i - 1:len(matrix[i - 1]) - i + 1][::-1])
            tracker[len(matrix) - i][i - 1:len(matrix[i - 1]) - i + 1] = [1 for v in matrix[len(matrix) - i][
                                                                                     i - 1:len(matrix[i - 1]) - i + 1]]

            if not any(True for lst in tracker if 0 in lst):
                break

            # bottom->top
            for lst in matrix[i:len(matrix) - i][::-1]:
                output.append(lst[i - 1])
                tracker[matrix.index(lst)][i - 1] = 1

            if not any(True for lst in tracker if 0 in lst):
                break

            i += 1

        return output

    '''
    This is doing basically the same thing as the solution I have come with even the time complexity is similar. However,
    the way they have achieved that was pretty interesting. Instead of keeping a tracker of which values are put into 
    output, this algorithm started trimming off the original matrix as we populate the output. This way we are saving 
    space, the code looks cleaner and there is no need for coming up with logic based on indices. Coming up with logic
    based on indices takes time as we have to figure out a pattern based on our desired behaviour not to mention problem
    with understanding the code later on. The strategy of popping items from the original matrix was fascinating.
    This solution was found from an youtube video which was originally submitted to LeetCode by another person. Shout
    out the person who came up with this strategy.
    '''
    def spiralOrder_clean(self, matrix: List[List[int]]) -> List[int]:
        output = []

        while matrix:
            # left -> right
            output += matrix.pop(0)

            # top -> bottom
            if matrix and matrix[0]:
                for row in matrix:
                    output.append(row.pop())

            # right -> left
            if matrix:
                output += matrix.pop()[::-1]

            # bottom -> top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    output.append(row.pop(0))

        return output


solution = Solution_54()
mat = [[int(z) for z in v.split(',')] for v in re.findall("\[([\d,]+)\]", input())]
print(solution.spiralOrder(mat))
print(solution.spiralOrder_clean(mat))
