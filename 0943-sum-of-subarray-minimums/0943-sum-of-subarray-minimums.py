class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        prev_less = [0]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_less[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        next_less = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_less[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        
        res = 0
        for i in range(n):
            res = (res + arr[i] * prev_less[i] * next_less[i]) % MOD
        
        return res