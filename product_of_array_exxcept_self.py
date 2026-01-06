# def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []
#         totalPre = []
#         totalPost = []

#         for i in range(len(nums)):
#             pre = [1]
#             post = [1]
            
#             for j in range((i+1),(len(nums))):
#                 post[0] *= nums[j]
#             totalPost.append(post[0])
#             for k in range(0,i):
#                 pre[0] *= nums[k]
#             totalPre.append(pre[0])
#         for i in range(len(totalPre)):
#             print(totalPre[i],totalPost[i])
#             output.append(totalPre[i] * totalPost[i])
#         return output


def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *=nums[i]
        
        return res