num=list(map(int,input().split()))
# sum=0
# for i in num:
#     sum=sum+i
#
# print(sum)
# print('length : ',len(num))
# for i in range(len(num)):
#     sum=sum+num[i]
#
# print(sum)
new_num = [int(x) for x in num]
print(sum(new_num))