import sys
input = sys.stdin.readline

'''
N일 ; T : 걸리는기간 ; P : 받을 수 있는 금액
'''
N = int(input())
appoint = [[0,0]] + [[] for _ in range(N)]
dp = [0] * (N + 1)
for i in range(1, N+1):
    T, P = map(int, input().split())
    appoint[i] = [T, P]

#  appoint = [[0, 0], [3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
# 최대 이익(P) 구하기

# 1~N 칸에 대해 이전 칸과 비교해서 더 큰 값 가져오기
for j in range(1, N+1):
    dp[j] = max(dp[j-1], dp[j])

    # 걸리는시간(당일포함) 
    next_t = appoint[j][0]-1
    # 다음 시간, 받을 금액
    next = j + next_t
    next_p = appoint[j][1]

    # 기존 누적값에 받을 금액 더한 것과, 현재 가진 값 비교 
    if next < N+1:
        dp[next] = max(dp[j-1] + next_p, dp[next])

print(max(dp))