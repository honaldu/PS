# if 연산자로 s 길이에 따른 return 생성
# try, except 로 int 함수 적용 값에 따른 return 생성

def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        try:
            int(s)
            return True
        except:
            return False
    else:
        return False


solution('123556')
