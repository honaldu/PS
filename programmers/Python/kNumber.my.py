# 배열 안에서 이터레이터를 이용하여 펼침
# index slicing 을 이용하여 배열 자름
# sorted 함수로 정렬 후 indexing 작업

def solution(array, commands):
    return [sorted(array[i[0]-1:i[1]])[i[2]-1]
            for i in commands]
