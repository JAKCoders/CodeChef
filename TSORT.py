n=int(input())
arr = []
for i in range(n):
    x=int(input())
    arr.append(x)
arr.sort()
for i in range(len(arr)):
    print(arr[i])