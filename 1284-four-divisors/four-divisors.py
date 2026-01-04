class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def isPrime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        total = 0

        for n in nums:
            root = int(round(n ** (1/3)))
            if root > 1 and root * root * root == n and isPrime(root):
                total += 1 + root + root * root + n
                continue

            sum_div = 0
            p = q = None
            d = 2
            while d * d <= n:
                if n % d == 0:
                    p = d
                    q = n // d
                    if p != q and isPrime(p) and isPrime(q):
                        sum_div = 1 + p + q + n
                    break
                d += 1
            total += sum_div

        return total