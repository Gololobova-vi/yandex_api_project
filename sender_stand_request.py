# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data

user_response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
print(user_response.status_code)

# Функция response.json() позволяет получить тело ответа в формате JSON.
print(user_response.json())


# Определение функции post_new_client_kit для отправки POST-запроса на создание нового набора
def post_new_client_kit(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_NAME,
                         json=body,
                         headers=data.headers_kit)


# Вызов функции post_new_client_kit с телом запроса для создания нового набора из модуля data
kit_response = post_new_client_kit(data.kit_body)

