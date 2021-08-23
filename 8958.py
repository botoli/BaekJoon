'''
풀이 시간: 21.08.23.Mon 22:29 ~ 22:43

문제 번호: 8958

참고 사이트: https://pacific-ocean.tistory.com/75

<문제>
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

<입력>
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

<출력>
각 테스트 케이스마다 점수를 출력한다.

<예제 입력>
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

<예제 출력>
10
9
7
55
30
''' 

'''
<내가 틀린 코드>

from sys import stdin

input = stdin.readline 
n = int(input())
quizAnswers = []

for i in range(n):
  quizAnswers = input()

for i in range(n): # 테스트 케이스의 수만큼 반복
  if find('O'):
'''

testcaseNumber = int(input())
for i in range(testcaseNumber):
  quizAnswer = input()
  listOfQuizAnswer = list(quizAnswer)
  sum = 0
  oNumber = 1
  for i in listOfQuizAnswer:
    if i == 'O':
      sum += oNumber
      oNumber += 1
    else:
      oNumber = 1
  print(sum)
