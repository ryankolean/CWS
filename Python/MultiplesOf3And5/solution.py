def solution(number):
    return sum(set(list(range(0, number, 3)) + list(range(0, number, 5))))