class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l =0
        num_zero = 0
        max_num = 0
        n = len(nums)
        for r in range(n):
            if nums[r]==0:
                k -= 1
            if k<0:
                if nums[l]==0:
                    k += 1
                l += 1
            w = r-l+1
            max_num = max(max_num,w)   
        return max_num
            