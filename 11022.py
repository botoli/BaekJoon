'''
풀이 시간: 21.08.24.Tue 08:03 ~ 08:06

문제 번호: 11022

<문제>
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

<입력>
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

<출력>
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

<예제 입력>
5
1 1
2 3
3 4
9 8
5 2

<예제 출력>
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
''' 

'''
예전에 내가 작성한 코드

https://www.acmicpc.net/problem/11022


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
'''

from sys import stdin

input = stdin.readline

n = int(input())

for i in range(n):
  a, b = map(int, input().split())
  print(f'Case #{i+1}: {a} + {b} = {a + b}')
