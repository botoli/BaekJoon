from sys import stdin

input = stdin.readline
N = int(input())

for i in range(N, 0, -1):
  print(' ' * (N-i)  + '*' * (2*i-1) + ' ' *(N-i))

# N 5 5 5 5 5 
# i 5 4 3 2 1
#   0 1 2 3 4
# * 9 7 5 3 1

for j in range(1, N):
  print(' '*(N-j-1) + '*'*(2*j+1) + ' '*(N-j-1))

# N 5 5 5 5 
# j 1 2 3 4
#   3 2 1 0
# * 3 5 7 9