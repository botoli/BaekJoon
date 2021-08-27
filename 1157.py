'''
풀이 시간: 21.08.25.Wed 23:00 ~ 23:30
          21.08.26.Thu 07:56 ~ 08:01

문제 번호: 1157

참고 사이트: https://ooyoung.tistory.com/70

<문제>
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

<입력>
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

<출력>
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

<예제 입력 1>
Mississipi

<예제 출력 1>
?

<예제 입력 2>
zZa

<예제 출력2>
Z
''' 

'''
<내가 작성한 코드(오답)>

from sys import stdin

input = stdin.readline
alphabet = input()
countLetter = 1
upperCaseLetter = 65
lowerCaseLetter = 97
largestAlphabet = 0

# 소문자와 대문자를 같은 문자로 볼 수 있는 방법

while range(26):
  if upperCaseLetter == alphabet.count(alphabet) and lowerCaseLetter == alphabet.count(alphabet):
    largestAlphabet = upperCaseLetter
'''

words = input().upper()
uniqueWords = list(set(words)) 

cnt_list = []
for x in uniqueWords :
    cnt = words.count(x)
    cnt_list.append(cnt)  
    
if cnt_list.count(max(cnt_list)) > 1 : 
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  
    print(uniqueWords[max_index])
