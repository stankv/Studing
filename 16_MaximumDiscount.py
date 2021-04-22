def MaximumDiscount(N, price):
    # сортируем массив по убыванию
    S = sorted(price, reverse = True)
    # каждый третий предмет даст макисмальную скидку при покупке этих 3-х предметов
    discount = 0
    for i in range(2, N, 3):
        discount += S[i]
    return discount