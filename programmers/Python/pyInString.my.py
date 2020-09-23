# string 소문자 변환, p,y 변수 확보, 이터러블로 String 내 p, y 숫자 파악 후 True/False return
# string 소문자로 변환, list 로 형태 변환, count 함수로 p,y 카운팅 값 return

def solution(s):
    return list(s.lower()).count('p') == list(s.lower()).count('y')
