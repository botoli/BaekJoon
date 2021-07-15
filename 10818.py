from sys import stdin

input = stdin.readline
n = int(input())

arr = list(map(int, input().split()))

maximum = arr[0]
minimum = arr[0]
for j in range(n):
  if maximum < arr[j]:
    maximum = arr[j]
  if minimum > arr[j]:
    minimum = arr[j]
    
print(minimum, maximum)
