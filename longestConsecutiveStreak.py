def longestStreak(nums):
    nums = sorted(nums)
    windowLen = 1
    result = 0
    i, j = 0, 1
    while j < len(nums):
        if nums[i] == nums[j]:
            i += 1
            j += 1
            continue
        elif nums[i] + 1 != nums[j]:
            result = max(result, windowLen)
            i = j
            j += 1
            windowLen = 1
        else:
            windowLen += 1
            i += 1
            j += 1
    result = max(result, windowLen)
    return result
