# 11-1 수 정렬하기(2750) : https://www.acmicpc.net/problem/2750

import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
print(num)

def comp(num, index):
    if index == 1:
        return
    i = len(num) - index
    for _ in range(index):
        if num[i] < num[i+1]:
            comp(num, index-1)
        else:
            num[i], num[i+1] = num[i+1], num[i]
comp(num, len(num))

# 중첩 for로 ...
# for i in range(len(num)):
#     for j in range(len(num)-i-1):
#         if j > len(num)-i:
#             break
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]




print(num)



