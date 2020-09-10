# 이터러블로 s 순환
# 내부 if 문으로 알파벳, 공백 구분
# join 함수로 병합
def solution(s, n):
    wordsList = []
    for i in s:
        if i == " ":
            wordsList.append(i)
        elif ord(i) + n > 122:
            97(ord(i)+n)-122
        wordsList.append()
    return str(''.join([chr(ord(i)+n) for i in s if ord(i)+n > 96]))


solution("AB", 1)
