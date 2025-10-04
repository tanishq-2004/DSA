from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements in an array except for the element at the current index.
        
        This method solves the problem in O(n) time complexity and O(1) extra space complexity
        by using a two-pass approach to calculate prefix and suffix products.
        """
        n = len(nums)
        # Initialize the answer array. This does not count as extra space.
        answer = [1] * n
        
        # --- Pass 1: Calculate prefix products ---
        # In this pass, answer[i] will store the product of all elements to the left of i.
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
            
        # --- Pass 2: Calculate suffix products and multiply with prefixes ---
        # In this pass, we multiply the existing prefix product in answer[i]
        # by the suffix product of elements to the right of i.
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
            
        return answer
