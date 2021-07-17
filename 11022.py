'''
https://www.acmicpc.net/problem/11022
'''

from sys import stdin
n = int(input())

sum = []
copyA = []
copyB = []
for i in range(n):
  a, b = list(map(int, input().split()))
  copyA.append(a)
  copyB.append(b)
  sum.append(a+b)
  
for j in range(0, n):
  print(f'{copyA[j]} + {copyB[j]} = {sum[j]}')
