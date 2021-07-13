'''
https://www.acmicpc.net/problem/2438
'''

from sys import stdin

input = stdin.readline
N = int(input())

for i in range(1 ,N+1):
  print('*' * i)