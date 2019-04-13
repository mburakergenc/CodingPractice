def reverseString(strng):
    # create 2 pointers i and j
    # i will start from 0
    i = 0
    # j will start from the last element of the string
    j = len(strng) - 1
    # temporary variable to swap i and j
    t = ""
    # swap the first and last element in the string until they meet in the middle
    while i < j:
        t = strng[i]
        strng[i] = strng[j]
        strng[j] = t
        j -= 1
        i += 1
    return strng

