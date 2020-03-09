T = int(input()) #test case number (1<=T<=50)

for test_case in range(1, T + 1):
    n = 10
    squareList = [[0]*n for _ in range(n)] #add 10*10 list
    N = int(input()) #coloring area number (2<=N<=30)
    cnt = 0
    for inner_case in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        #r1: left upside x, c1: left upside y, r2: right downside x, c2: right downside y, color: color
        if color == 1: #if color is red
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if squareList[i][j] == 1: #same color: union
                        squareList[i][j] = 1
                    else:
                        squareList[i][j] += 1
        if color == 2: #if color is red
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if squareList[i][j] == 2: #same color: union
                        squareList[i][j] = 2
                    else:
                        squareList[i][j] += 2

        #print(squareList)
    for i in range(10): #count purple(num 3)
        for j in range(10):
            if squareList[i][j] == 3:
                cnt += 1
    print("#" + str(test_case) + " " + str(cnt))
