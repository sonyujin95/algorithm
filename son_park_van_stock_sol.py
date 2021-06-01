def solution(prices):
    answer = [0] * len(prices)                  # price의 길이만큼 배열 answer을 생성
    
    for i in range(len(prices)):                # price의 길이만큼 반복
        
        for j in range(i+1, len(prices)):       # 배열의 i번쨰 index에서 남은 길이(초)동안 반복
            
            if prices[i] <= prices[j]:          # 가격이 떨어지는 것을 체크하여 answer 해당 인덱스의 값을 증가시키고
                answer[i] += 1
                
            else:
                answer[i] += 1
                break                           # 떨어진 경우 내부 반복문을 종료(더이상 증가시키지 않음)
                
    return answer                               # 저장된 answer를 return