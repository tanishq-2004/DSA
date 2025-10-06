class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0
        counts = collections.Counter()

        for right, char in enumerate(s):
            # Expand the window by including the character at the right pointer
            counts[char] += 1

            # Update the frequency of the most common character in the current window
            max_freq = max(max_freq, counts[char])

            # Check if the current window is invalid
            # A window is invalid if the number of characters to replace is > k
            window_length = right - left + 1
            if window_length - max_freq > k:
                # Shrink the window from the left
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            # The window size may not increase, but we track the max size seen
            max_length = max(max_length, right - left + 1)

        return max_length
