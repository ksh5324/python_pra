# def add(n):
#     return  n+n
#
# print(add(5))
# a=(lambda n:n+n)
# print(a(5))
#
# print((lambda n:n+5)(5))

# 숫자를 입력받아 정렬하여 출력한다.
# 이 때 중복된 숫자는 하나만 나오록 하시오
# 입력 : 4 5 1 2 3 4 3
# 출력 : 1 2 3 4 5
# n = list(map(int, input().split()))
# n.sort()
# for i in range(len(n)):
#     if(n[i]==n[i+1]):
#         pass
#     print(n[i]) // 틀림


n2 = list(map(int, input().split()))
n2 = set(n2)
print(n2)