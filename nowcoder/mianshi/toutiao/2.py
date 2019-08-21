import sys
b = sys.stdin.readline().strip()
value = list(map(int,b.split()))
length,recurent_num = value[0],value[1]
number = str(sys.stdin.readline().strip())
need_length = length
res_string = ''
for i in range(0,recurent_num):
    if need_length <= 0:
        break
    if i == 0:
        res_string = res_string + number[0]
        need_length = need_length - 1
    else:
        jieguo = int(res_string[0])
        for j in res_string[1::]:
            jieguo = jieguo ^ int(j)
        jieguo = int(number[i]) ^ jieguo
        res_string = res_string + str(jieguo)
        need_length = need_length - 1
if need_length > 0:
    for i in range(recurent_num,length):
        jieguo = int(res_string[i-recurent_num+1])
        for j in res_string[i-recurent_num+2::]:
            jieguo = jieguo ^ int(j)
        jieguo = int(number[i]) ^ jieguo
        res_string = res_string + str(jieguo)
        need_length = need_length - 1
print(res_string)







