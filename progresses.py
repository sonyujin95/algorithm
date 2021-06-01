def solution(progresses, speeds):
    import math
    from collections import Counter

    days=[]                                                   # list 생성
    for i in range(len(progresses)):                          # progresses의 길이만큼 반복
        days.append(math.ceil((100-progresses[i])/speeds[i]))    # 스피드 대비 진행과정(며칠) 리스트에 추가. 소수점 이하에 숫자가 있으면 소수점 이하 숫자를 없애고 1을 더한다.

    for i in range(len(days)):                           # days의 길이만큼 반복
        for j in range(i+1, len(days)):                  # 배열의 i번째 index에서 남은 길이(며칠) 반복
            if days[i]>days[j]:                         
                days[j]=days[i]                          # 남은 길이(며칠)가 소진되면 내부 반복문 종료

    return list(Counter(days).values())    # Counter 클래스로 값에 대해 리스트로 반환