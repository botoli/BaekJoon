'''
풀이 시간: 21.08.25.Wed 22:01 ~ 22:11

문제 번호: 11720

<문제>
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

<입력>
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

<출력>
입력으로 주어진 숫자 N개의 합을 출력한다.

<예제 입력>
1
1

<예제 출력>
1
''' 
from sys import stdin

input = stdin.readline
n = int(input())
string = int(input())
summary = 0

for i in str(string):
  summary += int(i)
print(summary)