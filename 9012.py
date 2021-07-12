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
    if vps[i] == '(':
      stack_push(stack, '(') 
    elif vps[i] == ')':
      if len(stack) == 0 :
        answer = False
        break
      last = stack_pop(stack)
      if last == '(':
        continue
  if len(stack) != 0:
    answer = False
  if answer:
    print('YES')
  else:
    print('NO')
