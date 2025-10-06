class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)



        for i in range(1,len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
           # print(prefix[i])

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix = postfix * nums[i]
            #print(postfix[i])

       

        return answer