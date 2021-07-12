# Проверка по коду результата, что отправка данных с помощью POST на сервер httpbin.org проходит корректно. 
import requests

# проверяем ответ сервера
response = requests.get('https://httpbin.org')
if response.status_code == 200:
    print("OK", response.status_code)
    # смотрим в заголовках в каком формате передаются данные (ключ Content-Type)
    result = response.headers
    print(result)
else:
    print("ERROR",response.status_code)

# отправляем на сервер произвольные данные и проверяем что отправка прошла корректно
response1 = requests.post('http://httpbin.org/post', data = {'UserId':'12345', 'Status':'On'})
if response1.status_code == 200:
    print("OK", response1.status_code)
else:
    print("ERROR",response1.status_code)