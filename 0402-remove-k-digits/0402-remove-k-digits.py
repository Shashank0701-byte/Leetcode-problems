class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        stack = stack[:-k] if k else stack
        res = ''.join(stack).lstrip('0')

        return res if res else '0'