# ПОИСК КЛЮЧЕВОГО КЛЮЧА ЧЕРЕЗ ТРАНСФОРМИРУЮЩУЮ ТРАНСФОРМАЦИЮ
def TransformTransform(A, N):

    # трансформирующая трансформация
    def S(A):
        B = []
        for i in range(len(A)):
            for j in range(len(A) - i):
                k = i + j
                ma = max(A[j:k+1], default=-1)
                if ma > -1:    # чтобы не писать нули в массив
                    B.append(ma)                    
        return B

    if sum(S(S(A))) % 2 == 0:
        return True
    else:
        return False