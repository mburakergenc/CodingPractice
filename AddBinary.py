def addBinary(a, b):
    # Turn strings into integers
    a = int(a, 2)
    b = int(b, 2)
    # if a and b is zero return 0 > 0+0=0
    if a == 0 and b == 0:
        return "0"
    # Since we now have integers, we can sum them up.
    n = a + b
    # Create empty strings to fill up later on
    strng = ""
    result = ""
    # Calculate the binary value of n
    while n:
        # Calculate the remainder of n % 2 and cast it to string
        remainder = str(n % 2)
        # Add remainder to the string variable
        strng += remainder
        # Divide n by 2
        n = n // 2
        # Take the last element in string variable and add it to result
        result = strng[::-1]
    return result