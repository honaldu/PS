# or 문을 통한 코드 줄이기
# 변수를 통한 반복 줄이기

def solution(s, n):
    string = ""
    for i in s:
        ascii = ord(i)
        plusAscii = ascii + n
        if i == " ":
            string += i
        elif((plusAscii > 90 and ascii < 91) or (plusAscii > 122)):
            string += chr(plusAscii-26)
        else:
            string += chr(plusAscii)
    return string


solution("z", 4)
