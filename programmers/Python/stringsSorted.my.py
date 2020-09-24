from operator import itemgetter


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x[n+1]))


print(solution(["abce", "abcd", "cdx"], 1))
