from collections import defaultdict

def solution(id_list, report, k):
    
    answer = [0] * len(id_list) # [0, 0, 0, 0]
    report = set(report)
    
    list_I_report = defaultdict(set) #{"muzi": {"frodo", "apeach"}}
    num_of_reported = defaultdict(int) #{"muzi": 1, "frodo": 1}

    suspended = []

    for r in report:
        do_report, be_reported = r.split()

        # 리포트 몇번 받았는지 체크
        # 딕셔너리 값 추가하는 방법
        num_of_reported[be_reported] += 1
        # set에 한개씩 추가
        list_I_report[do_report].add(be_reported)

        if num_of_reported[be_reported] == k:
            suspended.append(be_reported)

    for s in suspended:
        for i in range(len(id_list)):
            if s in list_I_report[id_list[i]]:
                answer[i] += 1

    return answer

    # https://programmers.co.kr/learn/courses/30/lessons/92334?language=python