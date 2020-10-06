# elif 는 이전 조건문이 거짓일 때 수행.

# 그리디인 이유
# 매 순간 최선인 방법 (중복제거, i-1,i+1 제거) 를 선택하여 최선의 방뻡 도출해 냄.

# set 함수를 통해 중복된 lost,reserve 서로 제거
# 제거된 reserve 이터러블
# if, elif 문을 통해 lost 요소 제거

# 배울 점
# 삭제해야하는 요소를 종류별로 나눔. (중복, i-1, i+1)
# 요소 리스트에서 순서 정함 (중복된 걸 먼저 지워야 for 문 돌리는데 차질이 없다는 걸 상황을 시뮬레이션 해 생각함)
# if, elif 를 정확히 파악하고 삭제함.

def solution(n, lost, reserve):
    delReser = set(reserve)-set(lost)
    delLost = set(lost)-set(reserve)
    for i in delReser:
        if i-1 in delLost:
            delLost.remove(i-1)
        elif i+1 in delLost:
            delLost.remove(i+1)
    return n-len(delLost)
