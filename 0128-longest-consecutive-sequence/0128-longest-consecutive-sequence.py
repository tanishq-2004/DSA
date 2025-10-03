class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sett = set(nums)
        for num in sett:
            if num-1 in sett:
                continue
            length = 1
            while num+length in sett:
                length += 1
            longest = max(longest,length)
        return longest