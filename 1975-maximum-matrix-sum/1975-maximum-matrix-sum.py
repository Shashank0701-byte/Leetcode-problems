class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_abs = 0
        neg_count = 0
        mn = float('inf')

        for row in matrix:
            for x in row:
                if x < 0:
                    neg_count += 1
                ax = abs(x)
                sum_abs += ax
                mn = min(mn, ax)

        if neg_count % 2 == 0:
            return sum_abs
        else:
            return sum_abs - 2 * mn