def ConquestCampaign(N, M, L, battalion):
    S = []
    for i in range(N):
        b = []
        for j in range(M):
            b.append(0)
        S.append(b)
        
    count = 0
    L2 = 0
    for i in range(L * 2):
        if i % 2 == 0:
            x = battalion[i] - 1
        else:
            y = battalion[i] - 1
        count = count + 1
        if count % 2 == 0:
            if x >= 0 and x < N and y >=0 and y < M and S[x][y] == 0:
                S[x][y] = 1
                L2 = L2 + 1
    if L2 == 0:
        return 0    
    
    Day = 1
    cell = N * M - L2
    while cell > 0:
        for i in range(N):
            for j in range(M):
                if S[i][j] == Day:
                    if (i + 1) < N and S[i + 1][j] == 0:
                        S[i + 1][j] = Day + 1
                    if (i - 1) >= 0 and S[i - 1][j] == 0:
                        S[i - 1][j] = Day + 1
                    if (j + 1) < M and S[i][j + 1] == 0:
                        S[i][j + 1] = Day + 1
                    if (j - 1) >= 0 and S[i][j - 1] == 0:
                        S[i][j - 1] = Day + 1

        for i in range(N):
            for j in range(M):
                if S[i][j] > Day:
                    cell -= 1
        Day += 1
        if Day > N * M:
            Day = N * M + 1
            break
    return Day