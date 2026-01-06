numsa = [2,20,4,10,3,4,5]
 
 
# def longest_consecutive(nums):
#     nums_map = {}
#     length=0
#     for num in nums:
#         if num not in nums_map:
#             nums_map[num] = True
#     for num in nums:
#         next = num
#         temp_length = 1
#         while next+1 in nums_map:
#             temp_length +=1
#             next+=1
#         length = max(length,temp_length)
#     return length 


def longest_consecutive(nums):
    nums_map = {}
    length=0
    for num in nums:
        if num not in nums_map:
            nums_map[num] = True
    for num in nums_map:
        next = num
        temp_length = 1
        if num-1 not in nums_map:
            while next+1 in nums_map:
                temp_length +=1
                next+=1
            length = max(length,temp_length)
    return length 
print(longest_consecutive(numsa))