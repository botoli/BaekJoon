'''
https://www.acmicpc.net/problem/1924
'''

from sys import stdin

input = stdin.readline
x,y = map(int, input.split())
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

if x==2:
  day = (31+y) % 7
  print(days[day-1])
elif x==4 or x==6 or x==9 or x==11:
  31+28+y








