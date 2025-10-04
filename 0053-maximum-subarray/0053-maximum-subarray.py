class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
    # Initialize both maxes to the first element of the array.
        current_max = nums[0]
        global_max = nums[0]

    # Iterate from the second element of the array.
        for i in range(1, len(nums)):
            num = nums[i]

            # Decide whether to start a new subarray or extend the existing one.
        # If current_max is negative, it's better to start fresh with num.
            current_max = max(num, current_max + num)
        
        # Update the overall global maximum if the new current_max is greater.
            if current_max > global_max:
                global_max = current_max
            
        return global_max