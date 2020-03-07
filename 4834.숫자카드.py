T = int(input()) #테스트 케이스 1<=T<=50
#각 줄마다 "#T" (T는 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
for i in range(1, T + 1):
    N = int(input())  # 카드 장수 5<=N<=100
    CardNumbers = list(input())  # 여백없이 N개의 숫자가 여백없이 주어진다. (0으로 시작 가능)
    Number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0~9까지 개수 세어 저장하는 리스트
    maxNum = 0 #카드 개수가 중복될 경우 가장 큰 숫자
    indexNum = 0 #카드 개수가 중복일 경우 가장 큰 숫자 개수의 인덱스
    #print("CardNumbers:", CardNumbers)
    for j in range(len(CardNumbers)):
        CardNumbers[j] = int(CardNumbers[j])
        if CardNumbers[j] == 0:
            Number[0] += 1
        elif CardNumbers[j] == 1:
            Number[1] += 1
        elif CardNumbers[j] == 2:
            Number[2] += 1
        elif CardNumbers[j] == 3:
            Number[3] += 1
        elif CardNumbers[j] == 4:
            Number[4] += 1
        elif CardNumbers[j] == 5:
            Number[5] += 1
        elif CardNumbers[j] == 6:
            Number[6] += 1
        elif CardNumbers[j] == 7:
            Number[7] += 1
        elif CardNumbers[j] == 8:
            Number[8] += 1
        elif CardNumbers[j] == 9:
            Number[9] += 1
    print("CardNumbers의 길이:", len(CardNumbers))
    print("CardNumbers:", CardNumbers)
    print("Number:", Number)

    for l in range(len(Number)): #개수 센 길이만큼
        if Number[l] >= maxNum: #가장 긴 길이와 해당 숫자의 길이를 비교해서 길거나 같을 경우
            maxNum = Number[l] #교체
            indexNum = l
    print("maxNum:", maxNum, ", index:", indexNum) #교체된 길이에 해당하는 숫자를 출력
    print("#" + str(i) + " " + str(indexNum) + " " + str(maxNum))
