# ПОИСК НАИМЕНЬШЕГО ИЗ ВСЕХ ЛЕКСИКОГРАФИЧЕСКИ БОЛЬШИХ СЛОВ, КОТОРЫЕ БОЛЬШЕ ЗАДАННОГО
# используется алгоритм Нарайаны, реализация подсмотрена здесь - https://prog-cpp.ru/permutation
def BiggerGreater(input_str):

    def swap(a, i1, i2):
        a[i1], a[i2] = a[i2], a[i1]

    def NextSet(a, n):
        j = n - 2
        while (j != -1 and a[j] >= a[j + 1]):
            j = j - 1
        if j == -1:
            return False    # больше перестановок нет
        k = n - 1
        while (a[j] >= a[k]):
            k = k - 1
        swap(a, j, k)
        l = j + 1 
        r = n - 1   # сортируем оставшуюся часть последовательности
        while (l < r):
            swap(a, l, r)
            l = l + 1
            r = r - 1
        return True

    a = list(input_str)
    n = len(a)
    S = []
    while(NextSet(a, n)):
        S.append(''.join(a))
    if len(S) == 0:
        return ""
    else:
        return ''.join(S[0])