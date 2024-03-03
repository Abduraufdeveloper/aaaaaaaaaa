# a = "ali"
# b = a.capitalize()
# print(b)
#
# name = "Jasur"
# print(name[0])
#

# names = "Jasur"
# print(names[::-1])
#
# for x in name:
#     print(x)
#
# while True:
#     num = int(input("Sonni kiriting: "))
#     print(1 - num)
#
#
#
# number = [1, 2, 3, 4, 6]

#Start:Stop:Step
# a = [1,2,3,4,5,6,7,8,9]
# print(a[::-1])
#
# for x in range(1, 100, 2):
#     if x == 97:
#         print("Bor")
#         break
#
# else:
#     print("Error!")

numbers = [2,4,6,1,3,5,9,7,-1]

n = len(numbers)
for x in range(0, n):
    for y in range(0, n - x - 1):
        if numbers[y] > numbers[y + 1]:
            numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]

print(numbers)






















