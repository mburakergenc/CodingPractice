def longestValidParentheses(s):
    # Init Max Longest Valid String
    res = 0
    # Create a stack with -1
    stack = [-1]
    # Traverse through the stack
    for i, j in enumerate(s):
        # If there is an opening paren push its index to the stack.
        if j == "(":
            stack.append(i)
        # If there is a closing paren, pop the last element from the stack
        else:
            stack.pop()
            # If the stack is empty append current element's index
            if len(stack) == 0:
                stack.append(i)
            # If the stack is not empty calculate the max by subtracting the last element in the stack
            # from the current element's index
            else:
                res = max(res, i - stack[(len(stack)-1)])
    return res
