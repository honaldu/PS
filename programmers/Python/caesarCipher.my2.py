# ASCII 코드를 이용한 시저 암호 해독.
# 빈 String 생성
# for 문으로 s 이터러블
# if 로 이터러블 제어
# ord, chr 함수로 ASCII 코드 제어

def solution(s, n):
    string = ""
    for i in s:
        ascii = ord(i)
        plusAscii = ascii + n
        if i == " ":
            string += i
        elif(plusAscii > 90 and ascii < 91):
            string += chr(plusAscii-26)
        elif(plusAscii > 122):
            string += chr(plusAscii-26)
        else:
            string += chr(plusAscii)
    return string


solution("z", 4)
