def minSubArrayLen(target: int, nums):
    # Define variables
    summation = 0
    start = 0
    # Define initial length and try to minimize it
    res = len(nums)+1
    # Loop through the array
    for index, val in enumerate(nums):
        # Sum the elements
        summation += val
        # When sum is equal to or greater than the target
        while summation >= target:
            # Update the lentgh each time
            res = min(res, index-start + 1)
            summation -= nums[start]
            start+=1
    if res <= len(nums):
        return res
    else:
        return 0