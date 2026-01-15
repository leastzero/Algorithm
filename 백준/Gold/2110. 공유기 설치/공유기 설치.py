import sys

def solution():
    answer = 0
    input = sys.stdin.readline

    # 1. 입력 파싱
    N, C = map(int, input().split())
    houses = [int(input()) for _ in range(N)]

    houses.sort() # 탐색을 위해 정렬

    # 2. 후보 거리 = 1 ~ (가장 오른쪽 집 - 가장 왼쪽 집)
    left = 1
    right = houses[-1] - houses[0]

    # 3. 이분 탐색 시작 (후보값 d, 설치 개수 count)
    while left <= right:
        d = (left + right) // 2

        # 1번 집부터 설치하는 게 최소한의 거리를 얻어내는 데 유리
        installed_house_x = houses[0]
        count = 1

        for i in range(1, N): # 돌면서 후보값보다 크거나 같으면 바아로 설치해버려
            if houses[i] - installed_house_x >= d:
                installed_house_x = houses[i]
                count += 1

        # 설치한 개수를 세서 C개인인지 체크
        # C개랑 같으면 바로 return 해야 하나..? 
        # -> 아닌듯. 왜냐하면 똑같이 C개 설치되었어도 더 짧은 거리가 있을 수도 있잖아
        # 아 그러네 왜냐하면 d는 just 임의로 지정한 후보값일 뿐이니까!!!!!

        if count >= C: # 공유기 개수보다 같거나 크면 거리를 늘려보자.
            answer = d
            left = d + 1
        else: # 아니면 거리를 좀 줄여보자 (언제 설치되나)
            right = d - 1

    return answer

print(solution())