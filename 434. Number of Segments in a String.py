# def countSegments(s):
#     count = 0
#     words = []
#     for i in range(len(s)-2):
#         if s[i].isalpha():
#             count+=1
#         else:
#             words.append(count)
#             count = 0
#     if len(words) == 0:
#         words.append(count)
#     return len(words)
#
# print(countSegments(""))

myString = "Hello"
myList = myString.split()

print(len(myList))