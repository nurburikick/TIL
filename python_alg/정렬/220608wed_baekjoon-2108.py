# https://www.acmicpc.net/problem/2108

import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
print(f'input_list: {num}')


# 정렬
# def comp(num, index):
#     if index == 1:
#         return
#     i = len(num) - index
#     for _ in range(index):
#         if num[i] < num[i+1]:
#             comp(num, index-1)
#         else:
#             num[i], num[i+1] = num[i+1], num[i]
# comp(num)
num.sort()
print(f'sorted_list: {num}')

# 평균
def n_mean(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
    return round( sum / len(num_list))


# 중앙값
def n_median(num_list):
    # idx = round(len(num_list)/2)
    idx = len(num_list)//2
    return num_list[idx]


# 최빈값
def n_mode(num_list):
    cnt_max_value = 0   # 최빈값
    smin_value = 0      # 여러 개 있을 때 최빈값 중 두 번째로 작은 값
    cnt_max = 0         # 최대 반복 횟수
    cnt = 1             # 현재 반복 횟수
    same = False        # 중복 체크
    for idx in range(len(num_list)-1):  # 5: 0~4
        if idx == 0:
            cnt_max_value = num_list[0]
            continue
        # 정렬이 되어 있어서 같거나 큰 경우만 있다.
        if num_list[idx-1] == num_list[idx]:
            cnt +=1
        elif num_list[idx] > num_list[idx-1]:   
            if cnt > cnt_max:
                cnt_max = cnt
                cnt_max_value = num_list[idx]
                same = False
            elif cnt == cnt_max:
                if num_list[idx] > cnt_max_value:
                    smin_value = cnt_max_value
                else:
                    smin_value = num_list[idx]
                same = True
            cnt = 1
    if same:
        return smin_value
    return cnt_max_value
                

# 범위       
def n_range(num_list):
    idx_min = 0
    idx_max = len(num_list)-1
    return num_list[idx_max]-num_list[idx_min]



# 실행
def main(nlist):
    if len(nlist) == 1:
        print(nlist[0], nlist[0], nlist[0], 0, sep='\n')
    else:
        print(n_mean(nlist))
        print(n_median(nlist))
        print(n_mode(nlist))
        print(n_range(nlist))

main(num)




