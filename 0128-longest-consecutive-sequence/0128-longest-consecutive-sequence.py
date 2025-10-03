class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)         # O(n) time, O(n) space
        longest = 0

        for num in num_set:
            # if num-1 is not present, num is the start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                # count consecutive numbers starting from current
                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
