# Pascal Triangle Rows:
# https://www.interviewbit.com/problems/pascal-triangle-rows/

def _generate_row(row_above, row_index):
    row = []
    # num of ints in each row == row_index + 1
    num_elements = row_index + 1
    for elem_index in xrange(num_elements):
        if elem_index == 0 or elem_index == num_elements - 1:
            row.append(1)
        else:
            row.append(row_above[elem_index - 1] + row_above[elem_index])
    return row


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        # input checking
        if A <= 0:
            return []
        elif A == 1:
            return [[1]]
        elif A == 2:
            return [[1], [1, 1]]
        
        # Now we can begin algorithm which assumes 
        # that length of rows is >= 2
        triangle = [[1], [1, 1]]
        for row_index in xrange(2, A):
            triangle.append(_generate_row(triangle[row_index - 1], row_index))

        return triangle
