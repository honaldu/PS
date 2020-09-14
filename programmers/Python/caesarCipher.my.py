# 이터러블로 s 순환
# 내부 if 문으로 알파벳, 공백 구분
# elif 분으로 알파벳 대,소 문자 분기 생성
# n 값에 따라 분기 생성

# join 함수로 병합
def solution(s, n):
    wordsString = ""
    for i in s:
        # 공백 시
        if i == " ":
            wordsString += i
        # 소문자
        elif(ord(i) > 96):
            A = chr(ord(i)+n)
            wordsString += A
        # 소문자 시
        else:
            A = chr(ord(i)+n)
            wordsString += A
    print(wordsString)


solution("AB", 1)
