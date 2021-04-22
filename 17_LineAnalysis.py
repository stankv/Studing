def LineAnalysis(line):
    # строка должна начинаться и заканчиваться "*"
    if line[0] != "*" or line[len(line) - 1] != "*":
        return False

    # проверяем отдельные исключительные случаи
    if line == "*" or line == "**" or line == "***":
        return True

    # определяем единый шаблон в строке
    template = ""
    for i in range(len(line)):
        template += line[i]
        if (line[i] != "*" and line[i + 1] == "*"):
            k = i + 1
            break
    if len(line) > 1:
        template += line[i + 1]

    # идем по строке и проверяем соответствие шаблону
    substr = ""
    flag = True
    if k <= (len(line) - 1):
        for i in range(k, len(line) - 1):
            substr += line[i]
            if line[i] != "*" and line[i + 1] == "*":
                substr += line[i + 1]
                if substr != template:
                    flag = False
                    break
                substr = ""
    return flag