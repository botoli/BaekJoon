'''
https://www.acmicpc.net/problem/10992
'''

from sys import stdin

input = stdin.readline
n = int(input())

print(' '* (n-1) + '*')
for i in range(1, n-1):
  print(' '*(n-i-1) + '*' + ' '*(2*i-1) + '*')

# n 1 2 3 4 5 6
#   0 0 1 2 3 4
# * 0
if n!=1:
  print('*' * (2*n - 1))
  