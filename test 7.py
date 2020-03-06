# 逢7就跳过游戏，过滤掉包含7或者7的倍数的数字

# 方法一
# for a in range(1,101):
#     if a % 7 == 0:
#         continue
#     elif a % 10 == 7:
#         continue
#     elif a // 10 == 7:
#         continue
#     print(a)

# 方法二
for a in range(1 , 101):
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
    print(a)