nums1 = [1, 3]
nums2 = [2, 4]


def findMedianSortedArrays(nums1, nums2):
    nums = [*nums1, *nums2]
    left = 0
    right = len(nums) - 1

    while left <= right:
        pass


print(findMedianSortedArrays(nums1, nums2))
