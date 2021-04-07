def odometer(N):
    time = 0
    time1 = 0
    S = 0
    count = 0
    for i in range(len(N)):
        if i % 2 == 0:
            velocity = N[i]
        else:
            time = N[i] - time1
            time1 = N[i]
        count = count + 1
        if count % 2 == 0 and count != 0:
            S = S + velocity * time
    return S