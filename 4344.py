'''
풀이 시간: 21.08.23.Mon 22:55 ~ 23:32
          21.08.24.Tue 07:13 ~ 07:51

문제 번호: 4344

<문제>
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

<입력>
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

<출력>
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

<예제 입력>
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

<예제 출력>
40.000%
57.143%
33.333%
66.667%
55.556%
''' 

from sys import stdin

input = stdin.readline 
c = int(input())
countNumber = 0

for i in range(c):
  studentNumberAndScore = list(map(int, input().split()))
  studentAverage = ( sum(studentNumberAndScore) - studentNumberAndScore[0] ) / ( len(studentNumberAndScore) - 1 )
  for j in range(studentNumberAndScore[0]):
    if studentNumberAndScore[j + 1] > studentAverage:
      # print(studentNumberAndScore[j + 1], studentAverage) 평균점수를 넘은 사람들의 수가 잘 카운팅 되는지 확인
      countNumber += 1
  aboveAverage = ( countNumber * 100 ) /  studentNumberAndScore[0]
  result = '{:.3f}'.format(aboveAverage)
  print(f'{result}%')
  studentNumberAndScore = []
  countNumber = 0
