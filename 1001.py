'''
풀이 시간: 21.08.24.Tue 08:19 ~ 08:23 

문제 번호: 1001

<문제>
두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

<입력>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

<출력>
첫째 줄에 A-B를 출력한다.

<예제 입력>
3 2

<예제 출력>
1
''' 
from sys import stdin

input = stdin.readline
a, b = map(int, input().split())

print(a - b)
