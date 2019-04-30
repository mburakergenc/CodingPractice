def pivotIndex(nums):
    leftSum = 0
    summation = sum(nums)
    for i, j in enumerate(nums):
        if leftSum == (summation - leftSum - j):
            return i
        leftSum += j
    return -1