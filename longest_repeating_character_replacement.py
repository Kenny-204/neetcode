# s = "ABAB"
# k = 2

# s = "XYYX"
# k = 2

s = "AAABABB"
k = 1
# s = "ABBB"
# k = 2
s = "AABABBA"
k = 1


def characterReplacement(s, k):
    count = {}
    left, right = 0, 0
    maxFreq = 0
    res = 0

    while right < len(s):
        if s[right] in count:
            count[s[right]] += 1
        else:
            count[s[right]] = 1

        maxFreq = max(maxFreq, count[s[right]])

        isValidWindow = ((right - left +1) - maxFreq) <= k
        if isValidWindow:
            right += 1
        else:
            count[s[left]] -= 1
            count[s[right]] -= 1
            left += 1
            maxFreq = max(maxFreq, count[s[right]])
        res = max((right - left ), res)

    return res


# def characterReplacement(s, k):
#     left, right = 0, 1
#     maxcount = 0

#     while right < len(s):
#         if s[left] == s[right]:
#             right += 1
#         else:
#             if k > 0:
#                 right += 1
#                 k -= 1
#             else:
#                 if s[left] == s[right]:
#                     left += 1
#                     k += 1
#                 else:
#                     left += 1

#         maxcount = max(maxcount, right - left)
#     return maxcount


# def characterReplacement(s, k):
#     left, right = 0, 1
#     maxcount = 0

#     while right < len(s):
#         if s[right] == s[left]:
#             right += 1
#         else:
#             while k > 0 and s[right] != s[left] and right < len(s)-1:
#                 right += 1
#                 k -= 1
#             if s[left] == s[right]:
#                 left += 1
#                 k += 1
#             else:
#                 left += 1
#         maxcount = max(maxcount, right - left + 1)
#     return maxcount


print(characterReplacement(s, k))
