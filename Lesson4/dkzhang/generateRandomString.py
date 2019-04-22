import random

def generateRandomString(max_len = 1024):
    str_len = random.randint(0, max_len)
    # print("str_len = ", str_len)

    a_z = "abcdefghijklmnopqrstuvwxyz"
    str_result = ""
    for i in range(0, str_len):
        str_result += a_z[random.randint(0, 26-1)]

    # print(str_result)
    return str_result

generateRandomString(100)

