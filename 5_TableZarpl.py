def SynchronizingTables(N, ids, salary):
    
    #ids_new = ids    # делаем копию массива для дальнейшей работы
    ids_new = []
    for i in range(N):
        ids_new.append(ids[i])
    
    #salary_new = salary
    salary_new = []
    for i in range(N):
        salary_new.append(salary[i])
    
    # сортируем оба списка по возрастанию
    xchange = True 
    while(xchange):
        xchange = False # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if ids_new[i] > ids_new[i+1]:
                ids_new[i], ids_new[i+1] = ids_new[i+1], ids_new[i]
                xchange = True

    xchange = True 
    while(xchange):
        xchange = False
        for i in range(N - 1):
            if salary_new[i] > salary_new[i+1]:
                salary_new[i], salary_new[i+1] = salary_new[i+1], salary_new[i]
                xchange = True
 
    for i in range(N):
        k = ids[i]    # читаем номер сотрудника
        # ищем в отсортированном массиве этот номер и получаем номер элемента
        for j in range(N):
            if ids_new[j] == k:
                salary[i] = salary_new[j]
                break
    
    return salary