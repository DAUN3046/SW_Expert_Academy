def binarySearch(l, r, search_page, cnt):
    c = int((l + r) / 2)
    if c == search_page:
        #print(cnt)
        return cnt
    elif c < search_page:
        l = c
        cnt += 1
        #print(cnt)
        #print("l:", l)
        return binarySearch(l, r, search_page, cnt)
    else:
        r = c
        cnt += 1
        #print(cnt)
        #print("r:", r)
        return binarySearch(l, r, search_page, cnt)

T = int(input()) #T: test case
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split()) #P: entire page, Pa: page A searches , Pb: page B searches

    case_A = binarySearch(1, P, Pa, 0) #A's binary search
    case_B = binarySearch(1, P, Pb, 0) #B's binary search
    #print("case_A:", case_A, ", case_B:", case_B)

    if case_A == case_B:
        print("#" + str(test_case) + " " + str(0))
    elif case_A < case_B:
        print("#" + str(test_case) + " A")
    else:
        print("#" + str(test_case) + " B")
