class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
           # print(prefix[i])


        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
            #print(postfix[i])

        for i in range(len(nums)):
            answer[i] = prefix[i] * postfix[i]

        return answer