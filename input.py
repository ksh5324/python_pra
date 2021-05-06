# num1=list(map(int, input().split()))
# print(num1)
# 숫자를 5~10사이의 숫자를 입력받을 때 1등과 꼬찌의 점수차를 출력하시오.
num1 = list(map(int, input().split()));
num1.sort()
num2 = len(num1)
print(num1[num2-1]-num1[0])
