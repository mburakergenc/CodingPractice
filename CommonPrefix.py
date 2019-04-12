def longestCommonPrefix(strs):
    if not strs:
        return ""
    # Get the alphabetically min word in a list of strings
    # if they have a match words in the middle will have too.
    minString = min(strs)
    # Get the alphabetically max word in a list of strings
    maxString = max(strs)
    # If the max string is longer
    # compare each letter and update the minString until there is no match with the maxString
    if len(minString) < len(maxString):
        for i, j in enumerate(minString):
            if j != maxString[i]:
                minString = minString[:i]
        return minString
    # If the min string is longer
    # compare each letter and update the maxString until there is no match with the minString
    else:
        for i, j in enumerate(maxString):
            if j != minString[i]:
                maxString = maxString[:i]
        return maxString