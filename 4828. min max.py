T = int(input())
for test_case in range(1, T + 1):
    T = int(input())
    numlist = list(map(int, input().split()))
    print("#"+str(test_case)+" "+str(max(numlist) - min(numlist)))