from L4_exercises.generateRandomString import generateRandomString
from L4_exercises.statisticsString import statisticsStringLength
from L4_exercises.statisticsString import statisticsStringChar
from L4_exercises.testPeakString import is_peak_string
import numpy as np
import matplotlib.pyplot as plt


def statisticsElement_niu(strs):
    D = dict.fromkeys(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z'], 0)
    for word in D:
        for m in range(len(strs)):
            D[word] += strs[m].count(word)
    return D


def main():
    print('this message is from main function')
    # test
    bigIntNum = 10000
    maxLen = 100
    strs = []
    for i in range(0, bigIntNum):
        theStr = generateRandomString(maxLen)
        strs.append(theStr)
        if is_peak_string(theStr) == True:
            print(theStr)

    list_length = statisticsStringLength(strs)

    # union test
    dict_char_zhang = statisticsStringChar(strs)
    dict_char_niu = statisticsElement_niu(strs)

    print(dict_char_zhang)
    print(dict_char_niu)

    a_z = "abcdefghijklmnopqrstuvwxyz"
    for s in a_z:
        if dict_char_zhang[s] != dict_char_niu[s]:
            print(s, dict_char_zhang[s], dict_char_niu[s])

    # array_length = np.array(list_length)
    # x = np.arange(0, len(list_length))
    # plt.plot(x, array_length)
    # plt.show()


if __name__ == '__main__':
    main()
