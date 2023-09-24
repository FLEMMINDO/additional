# def reverse(x):
#     x = str(x)[::-1]
#     if '-' in x:
#         x = x.replace('-', '')
#         if -int(x) < -2**31:
#             return 0
#         else:
#             return -int(x)
#     else:
#         if int(x) > 2**31 - 1:
#             return 0
#         else:
#             return int(x)
# print(reverse(-123))

def longestword(stroka):
    spisok = stroka.split(' ')
    print(max(spisok, key=len))

longestword('aaa eae gfdhfghfghfgh aewqewe asadzxcxzzxccw weqewew')