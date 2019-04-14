def twoSum(numbers, target):
    # Brute Force Method (Not efficient)
    # index1 = 0
    # index2 = 0
    # for i in range(len(numbers[:mid])):
    #     for j in range(1, len(numbers[:mid])):
    #         summation = numbers[i] + numbers[j]
    #         if summation == target and i != j:
    #             return i+1, j+1

    # Two Pointer solution (Just like reverse string solution)
    # First pointer starts from 0
    lower = 0
    # Second pointer starts at the end of the array
    upper = len(numbers) - 1
    # Iterate until we only have 2 numbers or target
    while lower < upper:
        # Check the upper and lower value of Numbers array if they are equal to the target
        # return their indexes (starting from 1 not 0)
        if numbers[lower] + numbers[upper] == target:
            return lower + 1, upper + 1
        # If the lower+upper is smaller than the target move the pointer that is at the beginning
        elif numbers[lower] + numbers[upper] < target:
            lower += 1
        # If the lower+upper is greater than the target move the pointer that is at the end of the array
        elif numbers[lower] + numbers[upper] > target:
            upper -= 1
