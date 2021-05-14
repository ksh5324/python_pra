stuNum=int(input())
height=[]
for i in range(stuNum):
    n=int(input())
    height.append(n)

height=sorted(height)
for i in height:
    print(i, end=' ')

#가장 큰 키 학생
print(height[-1])