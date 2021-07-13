'''
from sys import stdin

# 입력 빠르게 받기
input = stdin.readline

n = int(input()) 
# 띄어쓰기 오류가 날 때, 
rstrip(공백괴 개행문자를 없앰) 이용하기.
arr = list(map(int, input().split()))
'''
from sys import stdin

input = stdin.readline

A, B = map(int, input().split())
print(A+B)