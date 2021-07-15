'''
https://www.acmicpc.net/problem/10953
'''

from sys import stdin

input = stdin.readline
n = int(input())

arr = []
for i in range(n):
  a, b = map(int, input().split(','))
  arr.append(a+b)

for i in range(len(arr)):
  print(arr[i])
