# Напишите программу, в которой пользователь будет задавать две строки,
# а программа определять количество вхождений одной строки в другой

text1 = str(input('введите строку: '))
text2 = str(input('введите искомую строку: '))

# count = 0
# for i in range(len(text1) - len(text2) + 1):
#     if text1[i:i + len(text2)] == text2:
#         count += 1
# print(count)

print(text1.count(text2))

