class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in s.
        """
        # If the string is empty or already a palindrome, return it.
        if len(s) < 1 or s == s[::-1]:
            return s

        start = 0
        max_len = 1

        for i in range(len(s)):
            # Check for odd length palindromes centered at i
            # Example: "racecar"
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            # Check for even length palindromes centered between i and i+1
            # Example: "abba"
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
        
        return s[start : start + max_len]

# Example Usage:
solver = Solution()
print(f"Input: 'babad', Output: '{solver.longestPalindrome('babad')}'") # Expected: "bab" or "aba"
print(f"Input: 'cbbd', Output: '{solver.longestPalindrome('cbbd')}'")   # Expected: "bb"