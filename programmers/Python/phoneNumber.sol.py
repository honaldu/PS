# phoneNumber 자체를 편집함. 뒷 네자리 제외하고 별로 변환.
# return 에서 바로 문자열 편집함.

def solution(numbers):
    return "*"*(len(numbers)-4) + numbers[-4:]
