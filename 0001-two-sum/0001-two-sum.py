class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(nums):
            h[nums[i]] = i

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in h and h[compliment] != i:
                return [i,h[compliment]]
