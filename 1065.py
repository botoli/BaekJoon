'''
풀이 시간: 21.08.24.Tue 12:33 ~ 12:55
참고 사이트: https://www.acmicpc.net/board/view/25689
           21.08.24.Tue 22:14 ~ 23:21

문제 번호: 1065

<문제>
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

<입력>
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

<출력>
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

<예제 입력>
110

<예제 출력>
99
'''
from sys import stdin

input = stdin.readline
n = int(input())
countArithmeticSequence = 99

if n < 100:
  print(n)
else:
  for i in range(100, n + 1):
    firstValue = i // 100
    secondValue = ( ( i % 100 ) - ( i % 10 ) ) // 10
    thirdValue = i % 10
    commonDifference = secondValue - firstValue
    if ( secondValue + commonDifference ) == thirdValue: 
      # print(firstValue) 첫 번째 수
      # print(secondValue) 첫 번째 수 + 공차
      # print(thirdValue) 첫 번째 수 + 공차 + 공차
      countArithmeticSequence += 1
  print(countArithmeticSequence)
