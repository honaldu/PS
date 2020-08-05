# 방법에 대해 논해야 한다. 솔루션 찾기니까 하나의 솔루션에 잡혀있지 말고 자유롭게 생각하자.
# 풀이
# 큰 논리는 list 를 만나고 조건에 맞게 변수를 넣은 후 나눈다.


# 리스트 하나 생성
score_list = []
# 5만큼의 반복문 생성
for i in range(5):
    # 각 반복문에서 변수 생성 및 조건에 따라 변형 후 리스트에 삽입
    score = int(input())
    if(score) >= 40:
        score_list.append(score)
    else:
        score_list.append(40)
# sum으로 다 합하고 5로 나눈후 소숫점 제거
print(round(sum(score_list)/5))
