import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n # 최장수열 길이 저장

# LIS 길이 계산
for i in range(n):
    for j in range(i): # 나보다 앞에 있는 원소들 확인
        if a[i] > a[j]: # 내 앞 원소보다 내가 더 크면
            dp[i] = max(dp[i], dp[j]+1) # j번째 원소에 저장된 최장수열길이 + 1 저장 (나를 포함하기 때문에)

print(max(dp)) # 최장수열길이 출력

subsequence = [] # 최장 수열 저장
current_len = max(dp) # 찾아야 할 수열의 길이

# 역추적
for i in range(n-1, -1, -1):
    if dp[i] == current_len: # 만약 찾는 수열의 길이와 일치하는 dp 값을 가진 원소라면
        subsequence.append(a[i])
        current_len -= 1 # 찾을 수열의 길이 - 1

subsequence.reverse() # 역순이므로 뒤집기
print(*subsequence)