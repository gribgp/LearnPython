def statisticsStringLength(strs):
    max_len = 0
    for s in strs:
        if len(s) > max_len:
            max_len = len(s)
    print("max_len = ", max_len)

    list_length = [0 for i in range(0, max_len + 1)]

    for s in strs:
        list_length[len(s)] += 1

    return list_length


def statisticsStringChar(strs):
    a_z = "abcdefghijklmnopqrstuvwxyz"
    dictChar = {s: 0 for s in a_z}

    for s in strs:
        for ss in s:
            dictChar[ss] += 1
    return dictChar
