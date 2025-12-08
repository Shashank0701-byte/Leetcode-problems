class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        lsum = sum(cardPoints[:k])
        rsum = 0
        max_sum = lsum

        right = n - 1

        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[right]
            right -= 1
            max_sum = max(max_sum, lsum + rsum)

        return max_sum