'''
풀이 시간: 21.08.27.Fri 23:12 ~ 24:00
          21.08.28.Sat 07:04 ~ 07:29

문제 번호: 1152

<문제>
영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

<입력>
첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.

<출력>
첫째 줄에 단어의 개수를 출력한다.

<예제 입력>
The Curious Case of Benjamin Button

<예제 출력>
6
'''
from sys import stdin

input = stdin.readline
sentence = list(input())
countWord = 0

# 문장 길이 만큼 반복하며 문장의 공백을 찾고(앞 뒤 제외) 1을 더하면 단어의 개수가 된다.
for i in range(len(sentence)):
  if sentence[i] == ' ' and sentence[i + 1] == ' ':
    break
  elif sentence[i] == ' ':
    countWord += 1

if sentence[0] == ' ' and sentence[i-1] == ' ':
  print('앞 뒤 공백이 두개일 때:', countWord - 1) # 왜 인지는 모르겠지만 문자열의 끝은 공백이 아닌 다른 무언가가 저장되어있는 것 같다. 따라서 마지막 인덱스 전으로 해야 올바르게 공백인지 아닌지가 구분이 된다.
elif sentence[0] == ' ' or sentence[i-1] == ' ':
  print('앞 뒤 공백이 한개일 때:', countWord)
else:
  print('앞 뒤 공백이 없을 때:', countWord + 1)

# Mazatneunde Wae Teullyeoyo 
#Teullinika Teullyeotzi 