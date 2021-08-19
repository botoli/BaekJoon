'''
틀린 코드

from sys import stdin

input = stdin.readline

arr = []
while True:
  a, b = map(int, input().split())
  arr.append(a+b)

for i in range(len(arr)):
  print(arr[i])
'''

'''
시각: 21.08.19.Thu 22:23

문제번호: 10951번
참고 사이트: https://gomguard.tistory.com/122

참고한 사유: 원하는 만큼 값을 받고 출력하는 과정을 어떻게 구현해야 할지 감이 잡히지 않아 풀이를 참고함.

해결방법: 예외처리(try except)를 이용
'''

'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

<입력>

입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

<출력>

각 테스트 케이스마다 A+B를 출력한다.

'''

from sys import stdin

input = stdin.readline

while True:
  try:
    a, b = map(int, input().split())
    print(a + b)
  except:
    break


