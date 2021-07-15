from sys import stdin

input = stdin.readline

arr = []
while True:
  a, b = map(int, input().split())
  arr.append(a+b)

for i in range(len(arr)):
  print(arr[i])
