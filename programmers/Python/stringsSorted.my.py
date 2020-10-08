# 논리
# 발문에 주의 하자. 사전 순 이라는 부분에 주목하지 못 함.

# 정렬 먼저 실시해서 사전 순에 맞춤.
# n 번째 글자에 따른 정렬



from operator import itemgetter


def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


print(solution(["abce", "abcd", "cdx"], 1))
