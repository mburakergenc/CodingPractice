def removeElement(nums, val):
    # Length of the list
    n = len(nums)
    # Loop counter
    i = 0
    # Check every element in the list
    while(i<n):
        # if an element is equal to the target value
        if nums[i] == val: # delete it in place
            del(nums[i]) # Decrease the list length
            n-=1
        # If an element is not equal to the target value
        # Continue iterating till the end of the list
        else:
            i+=1

    return nums