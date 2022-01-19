def find_days(temps):
    answer = [0] * len(temps)
    stack = []

    # enumerate 함수를 사용하면 tuple 형식으로 index, value 값을 다 넣을 수 있다.
    for index, temp in enumerate(temps):
        print('tuple', index, temp)
        while stack and temp > temps[stack[-1]]:
            last = stack.pop()
            print('last', last)
            answer[last] = index - last
            print('answer', answer[last])
        # 스택에 아무값도 없으면 와서 먼저 index 값들을 스택에 넣어주게 된다.
        stack.append(index)
        print(stack)

    return print(answer)

find_days(temps=[78, 73, 55, 78, 90, 88, 75, 77])