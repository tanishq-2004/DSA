class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0  # where the next non-zero should go

        # Step 1: Move all non-zeros to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Step 2: Fill the remaining positions with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
