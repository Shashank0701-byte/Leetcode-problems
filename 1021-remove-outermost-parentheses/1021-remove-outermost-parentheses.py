class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = []

        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append('(')
                depth += 1
            else:  
                depth -= 1
                if depth > 0:
                    result.append(')')
        
        return "".join(result)