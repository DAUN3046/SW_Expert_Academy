def specialSort(numList):
    numList2 = []
    for i in range(5):
        numList2.append(a[-1 - i])  # +big num
        numList2.append(a[i])  # +small num
    return numList2

T = int(input()) #T: test case, 1<=T<=50
for test_case in range(1, T + 1):
    N = int(input()) #N: integer num
    a = list(map(int, input().split())) #10<=N<=100, 1<=aj<=100
    a.sort()  # small~big num sort
    b = specialSort(a)
    #print(specialSort(a))
    #print(b)
    print("#"+str(test_case), b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9])
