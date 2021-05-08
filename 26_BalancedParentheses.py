# ВСЕ ПРАВИЛЬНЫЕ КОМБИНАЦИИ ОТКРЫВАЮЩИХ И ЗАКРЫВАЮЩИХ СКОБОК
def BalancedParentheses(N):
    S = []

    def printParenthesis(str, pos, n, open, close):
        if(close == n):
            count = 0
            for i in str:
                S.append(i)
                count += 1
                if count == 2 * n:    # добавляем в конец "слова" пробел для разделения комбинаций
                    S.append(" ")
            return
        else:
            if(open > close):
                str[pos] = ')'
                printParenthesis(str, pos + 1, n, open, close + 1)
            if(open < n):
                str[pos] = '('
                printParenthesis(str, pos + 1, n, open + 1, close)

    if N > 0:
        str1 = [""] * 2 * N
        printParenthesis(str1, 0, N, 0, 0)
        stroka = "".join(S)
        stroka = stroka.rstrip()
    return stroka