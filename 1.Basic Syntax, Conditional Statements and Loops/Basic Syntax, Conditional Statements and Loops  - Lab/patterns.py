# Method 1
# number = int(input())
# for i in range(1, number + 1):
#     for j in range(0, i):
#         print("*", end="")
#     print()
#
#
# for i in range(number - 1, 0, - 1):
#     for j in range(0, i):
#         print("*", end="")
#     print()

# Method 2
number = int(input())
for i in range(1, number + 1):
    print(i * "*")
for j in range(number - 1, 0, - 1):
    print(j * "*")