"""
소괄호, 중괄호, 대괄호가 들어간 문자열이 vps인지 확인하기.
"""

import sys

def stack_push(stack, value):
  stack.append(stack)

def stack_pop(stack):
  last = stack.pop()
  return last

T = int(sys.stdin.readline())
for j in range(T):
  stack = []
  answer = True
  vps = sys.stdin.readline().strip()
  for i in range(len(vps)):
    if vps[i] == '(' or vps[i] =='{' or vps[i] =='[':
      stack_push(stack, vps[i]) 
    elif vps[i] == ')' or vps[i] == '}' or vps[i] == ']':
      if len(stack) == 0 :
        answer = False
        break
      last = stack_pop(stack)
      if last == '(' or last == '{' or last == '[':
        continue
  if len(stack) != 0:
    answer = False
  if answer:
    print('YES')
  else:
    print('NO')

