class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        maxFreq = 0
        ans = 0
        
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1
            maxFreq = max(maxFreq, freq[idx])

            # if replacements needed > k, shrink window
            while (r - l + 1) - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans