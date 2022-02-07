import re

def solution(phone_number):
    answer = ''

    # r은 왜 쓰는 거지?
    # -> r은 Raw String의 준말 백슬래시 문자를 해석하지 않고 남겨둠

    pattern = '\d(?=\d{4})'
    answer = re.sub(pattern, '*', phone_number)


    return print(answer)

solution("01033334444")

def solution_2(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]