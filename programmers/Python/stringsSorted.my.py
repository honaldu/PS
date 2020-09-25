# 논리
# n 번째 글자에 따른 정렬
# 그 다음 글자가 있을 경우 그에 따른 정렬


from operator import itemgetter


def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


print(solution(["abce", "abcd", "cdx"], 1))
