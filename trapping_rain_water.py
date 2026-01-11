height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(height):
    if not height:
        return 0
    total_rain_water = 0
    left = 0
    right = len(height) - 1
    max_left = height[left]
    max_right = height[right]

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(height[left], max_left)
            total_rain_water += max_left - height[left]

        else:
            right -= 1
            max_right = max(max_right, height[right])
            total_rain_water += max_right - height[right]
    return total_rain_water


print(trap(height))
