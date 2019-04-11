def addBinary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    if a == 0 and b == 0:
        return "0"
    n = a + b
    strng = ""
    result = ""
    while n:
        remainder = str(n % 2)
        strng += remainder
        n = n // 2
        result = strng[::-1]
    return result