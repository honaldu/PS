# string split 함수로 커팅
# upper 문자 활용
# 이터러블로 stringList 내부 글자 list 안에 분리하며 index 값 마다 upper 함수로 대문자화
# join 함수로 합체

def solution(string):
    stringList = string.split()
    devidedList = [[list(j) for j in i]for i in stringList]
    capitalized = [[[j.upper() for l in j]for j in i]for i in devidedList]
    print([[[j.upper() for l in j]for j in i]for i in devidedList])


solution("try hello world")
