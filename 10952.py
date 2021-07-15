from sys import stdin

input = stdin.readline

arr = []
while True:
  a, b = map(int, input().split())
  arr.append(a+b)
  if a==0 and b==0:
    break

for i in range(len(arr)-1):
  print(arr[i])
