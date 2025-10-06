from collections import Counter

class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:

    """
    Checks if s2 contains a permutation of s1.
    """
    len1, len2 = len(s1), len(s2)

    # Edge case: s1 cannot be a substring of s2 if it's longer.
    if len1 > len2:
        return False

    # Create frequency maps for s1 and the initial window in s2.
    s1_map = Counter(s1)
    window_map = Counter(s2[:len1])

    # Check if the very first window is a match.
    if s1_map == window_map:
        return True

    # Slide the window across the rest of s2.
    for i in range(len1, len2):
        # Add the new character entering the window from the right.
        window_map[s2[i]] += 1

        # Remove the old character leaving the window from the left.
        left_char = s2[i - len1]
        if window_map[left_char] == 1:
            del window_map[left_char]
        else:
            window_map[left_char] -= 1
        
        # After each slide, check for a match.
        if s1_map == window_map:
            return True
            
    return False
