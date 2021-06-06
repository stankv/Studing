import json
import requests

# 1. Получаем JSON-набор через внешний API. Сохраняем в файл.
response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)    # десериализация полученных данных

with open("E:/PROG/4/file1.json", "w") as json_file:
    json.dump(result, json_file, indent=2)    # сериализация и запись в файл

# 2. Подсчет количества уникальных пользователей в этом наборе
with open("E:/PROG/4/file1.json", "r") as json_file:
    json2 = json.load(json_file)    # открытие файла на чтение и десериализация данных
List_userId = []
for ani in json2:
    List_userId.append(ani["userId"])    # заносим в рабочий список все userId нашего набора
Temp = []    # удаление одинаковых элементов из рабочего списка
for i in List_userId:
    if i not in Temp:
        Temp.append(i)
List_userId = Temp
print("Количество уникальных пользователей:", len(List_userId))

# 3. Количество оригинальных задач у каждого пользователя и сколько их выполнено
user = {}
for k in range(1, len(List_userId) + 1):
    user[k] = { "num":0, "completed":0 }
    for i in range(len(result)):
        if result[i]["userId"] == k:
            user[result[i]["userId"]]["num"] += 1
            if result[i]["completed"] == True:
                user[result[i]["userId"]]["completed"] += 1

print("ID: ", "Задач: ", "Выполнено: ")    # форматированный вывод результата
for i in range(1, len(user) + 1):
    print("%2d%6d%10d" % (i, user[i]["num"], user[i]["completed"]))