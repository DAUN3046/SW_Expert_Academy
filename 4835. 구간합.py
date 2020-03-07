T = int(input()) #테스트 케이스 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 정수의 개수 N, 구간의 개수 M
    a = list(map(int, input().split()))  # N개의 정수 a들 공백으로 구분하여 리스트화
    sumNum = 0  # 구간합 계산시 필요한 변수
    NumList = []  # 구간합계산결과값들 저장하는 리스트
    for i in range(N - M + 1): #N-M만큼 반복
        for j in range(i, i + M): #이웃한 M개만큼 a[j] 합하기
            sumNum += a[j]
        NumList.append(sumNum) #리스트에 추가
        sumNum = 0 #구간합 초기화
    #print("sumNum:", sumNum,", NumList:", NumList)
    print("#" + str(test_case) + " " + str(max(NumList) - min(NumList)))