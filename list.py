myList=[
    ('BTS', 3),
    ('소녀시대', 2),
    ('엑소', 4),
    ('a', 1)
]
myList.sort()
print(myList)
myList.sort(key=lambda x:x[1])
print(myList)

num1=list(map(int, input().split()))
