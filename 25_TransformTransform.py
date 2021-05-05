# ПОИСК КЛЮЧЕВОГО КЛЮЧА ЧЕРЕЗ ТРАНСФОРМИРУЮЩУЮ ТРАНСФОРМАЦИЮ
def TransformTransform(A, N):

    # трансформирующая трансформация
    def S(A):
        B = []
        for i in range(len(A) - 1):
            for j in range(len(A) - i - 1):
                k = i + j
                B.append(max(A[j:k], default=0))
        return B

    if sum(S(S(A))) % 2 == 0:
        return True
    else:
        return False