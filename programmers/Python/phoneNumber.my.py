# answer 에 별과 phoneNumber 을 넣어서 출력함.

def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + \
        phone_number[len(phone_number)-4:len(phone_number)]
    return answer
