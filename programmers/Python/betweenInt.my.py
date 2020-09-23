# 등차수열 합 공식 이용
# 항의 수는 abs 함수를 이용해 절대값 구한 후 +1 해줌
# // 로 나머지 제외

def solution(a, b):
    return (abs(b-a)+1)*(a+b)//2
