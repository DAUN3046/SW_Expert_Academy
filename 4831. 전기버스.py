T = int(input())  # 첫 줄에 노선 수 T가 주어진다.
for i in range(1, T + 1):  # 각 케이스를 반복
    K, N, M = map(int, input().split())  # 각 노선별로 K, N, M이 주어지고
    M = list(map(int, input().split()))  # 다음줄에 M개의 정류장 번호가 주어진다.
    energy = K + 1  # energy가 K로 시작.
    n = 0  # 충전횟수
    for j in range(0, N + 1):  # 종점에 도착할 때까지
        energy -= 1
        if energy < 0:
            n = 0
        elif ((M[0] >= j - K) and (M[0] <= j) == True):  # 들르는 곳마다 다 충전하는 경우
            n += 1
            energy = K  # K - (j - M)
            del M[0]
        print(j, "번째의 energy:", energy, ", 충전횟수:", n, ", 충전소 리스트: ", M)
    print("#" + str(i) + " " + str(n))