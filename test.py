# 입력 1 2 3 4
# 입력 후 바로 배열 arr에 넣고 싶다.
arr=list(map(int, input().split()))
# int arr[] = {1,2,3,4};
for i in range(len(arr)):
    print('arr[', i, ']', arr[i])

