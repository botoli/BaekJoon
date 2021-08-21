'''
풀이 시간: 21.08.21.Sat 22:54 ~ 23:14

문제 번호: 3052
참고 사이트: https://pacific-ocean.tistory.com/35

<문제>
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

<입력>
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

<출력>
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

<예제 입력>
1
2
3
4
5
6
7
8
9
10

<예제 출력>
10

''' 

'''
<내가 작성한 코드(오답)>

from sys import stdin

input = stdin.readline
remainderArray = []
compareRemainder = 0

for i in range(10):
  n = int(input())
  n = n % 42
  remainderArray.append(n)

countNumber = 0
for i in range(10):
  compareRemainder = remainderArray[i]
  for j in range(i, 10):
    if remainderArray[i] == compareRemainder:
      countNumber += 1
      print()
  
print(countNumber)
'''

remainderArray = []
for i in range(10):
    n = int(input())
    remainderArray.append(n % 42)
remainderArray = set(remainderArray)
print(len(remainderArray))