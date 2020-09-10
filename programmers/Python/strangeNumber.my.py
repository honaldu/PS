# split 함수로 s 분리
# 내부 이터러블로 enumerate함수를 이용한 index, 값 추출
# index 값에 따라 대문자, 소문자 화
# join 함수로 병합

def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])


solution("try hello world")
