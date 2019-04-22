
def is_peak_string(theStr):
    strLen = len(theStr)

    if strLen < 3:
        return False

    if theStr[1] < theStr[0]:
        return False

    for i in range(1, strLen-1):
        # Find the peak
        if theStr[i+1] < theStr[i]:
            # Check Previous
            if theStr[i-1] == theStr[i]:
                return False

            # Confirm downhill
            for j in range(i+1, strLen-1):
                if theStr[j+1] > theStr[j]:
                    return False
            return True
    return False

