from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
            
        for char in ransomNote:
            if char not in counter:
                return False
            elif counter[char]==1:
                del counter[char]
            else:
                counter[char] -= 1
        return True
