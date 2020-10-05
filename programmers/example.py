n = 5
lost = [2, 4]
reserve = [1, 3, 5]

for number in lost:
    if number in reserve:
        reserve.remove(number)
        lost.remove(number)
        continue
    elif number-1 in reserve:
        reserve.remove(number-1)
        lost.remove(number)
        continue
    elif number+1 in reserve:
        reserve.remove(number+1)
        lost.remove(number)
        continue
