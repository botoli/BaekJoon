'''
작성일시: 21.08.19.Thu 22:39 ~ 21.08.20.Fri 22:38 

문제번호: 1110번

참고 사이트: https://wook-2124.tistory.com/222

0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

<입력>
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

<출력>
첫째 줄에 N의 사이클 길이를 출력한다.

<예제 입력>
26

<예제 출력>
4
'''

'''
내가 작성한 코드 (오답)

from sys import stdin

input = stdin.readline

originalNumber = int(input()) # 처음 입력한 값
nextNumber = -1 # 주어진 조건에 의해 연산된 값
countNumber = 0 # 원래 값으로 돌아오는 사이클 수


while originalNumber != nextNumber :
  nextNumber = (originalNumber % 10) * 10 + ( (originalNumber / 10 + originalNumber % 10) % 10 )
  countNumber += 1

print(countNumber)  
'''
'''
정답 코드

originalNumber = int(input())
nextNumber = originalNumber
cnt = 0

while True:
  ten = nextNumber // 10
  unit = nextNumber % 10
  c = (ten + unit) % 10
  nextNumber = (unit * 10) + c

  cnt = cnt + 1
  if(nextNumber == originalNumber):
    break

print(cnt)
'''
from sys import stdin

input = stdin.readline

originalNumber = int(input()) # 처음 입력한 값
nextNumber = originalNumber # 주어진 조건에 의해 연산된 값
countNumber = 0 # 원래 값으로 돌아오는 사이클 수

while True :
  ten = nextNumber // 10 # originalNumber를 사용하면 무한 루프에 빠지게 된다.
  unit = nextNumber % 10
  unitOfNextNumber = (ten + unit) % 10
  nextNumber = (unit * 10) + unitOfNextNumber
  countNumber += 1
  if originalNumber == nextNumber:
    break

print(countNumber)  
