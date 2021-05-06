# 시험 점수를 입력받았을 때 1등의 점수를 출력하는 프로그램을 작성하시오.
numLIst=[15,22,8,79,10,8,56,89]
numLIst.sort()#오름차순 정렬
print(numLIst)
print(numLIst[0])#가장 낮은 점수

numLIst.sort(reverse=True)#내림차순 정렬
print(numLIst)
print('1등의 점수 :',numLIst[0])#가장 높은 점수

print(len(numLIst))

num1=[1,2,3,4,5,7,3,4,8]
num2=len(num1)
num1.sort()
print(num1[num2-1]-num1[0])


