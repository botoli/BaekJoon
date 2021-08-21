'''
풀이 시간: 21.08.21.Sat 22:09 ~ 22:22

문제 번호: 2562

<문제>
개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

<입력>
3
29
38
12
57
74
40
85
61

<출력>
85
8

''' 

from sys import stdin

input = stdin.readline
nineNumber = []
maximum = -1
countMaximum = 0

for i in range(9):
  n = int(input())
  nineNumber.append(n)
  if nineNumber[i] > maximum:
    maximum = nineNumber[i]
    countMaximum = i

print(maximum)
print(countMaximum + 1)