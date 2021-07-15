'''
https://www.acmicpc.net/problem/11021
'''

from sys import stdin

input = stdin.readline
n = int(input())

arr = []
for i in range(n):
  a, b = map(int, input().split())
  arr.append(a + b)

for i in range(1, n+1):
  print(f'Case #{i}:', arr[i-1])