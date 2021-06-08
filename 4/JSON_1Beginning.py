import json
import requests

# Получаем JSON-набор через внешний API. Сохраняем в файл.
response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)    # десериализация полученных данных
with open("E:/PROG/4/file1.json", "w") as json_file:
    json.dump(result, json_file, indent=2)    # сериализация и запись в файл

# Подсчет количества уникальных пользователей, количества оригинальных 
# задач у каждого пользователя и сколько их выполнено
print("ID: ", "Задач: ", "Выполнено: ")
user = {}
user[result[0]["userId"]] = {"num":1, "completed":0}
for i in range(1, len(result)):
    if result[i]["userId"] == result[i - 1]["userId"]:
        user[result[i]["userId"]]["num"] += 1
        if result[i]["completed"]:
            user[result[i]["userId"]]["completed"] += 1
    else:
        print("%2d%6d%10d" % (result[i - 1]["userId"], user[result[i - 1]["userId"]]["num"], user[result[i - 1]["userId"]]["completed"]))
        user[result[i]["userId"]] = { "num":1, "completed":0 }
        if result[i]["completed"]:
            user[result[i]["userId"]]["completed"] +=1
print("%2d%6d%10d" % (result[i]["userId"], user[result[i]["userId"]]["num"], user[result[i]["userId"]]["completed"]))
print("Количество уникальных пользователей:", len(user))