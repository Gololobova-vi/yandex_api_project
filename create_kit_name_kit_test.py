# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


# эта функция меняет значение в параметре auth_token
def get_new_user_token(user_response):
    return user_response.json().get("authToken")


data.headers_kit["Authorization"] = "Bearer " + get_new_user_token(sender_stand_request.user_response)


# эта функция меняет значения в параметре name
def get_kit_body(kit_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body_kit = data.kit_body.copy()
    # изменение значения в поле name
    current_body_kit["name"] = kit_name
    # возвращается новый словарь с нужным значением kitName
    return current_body_kit


# Функция для позитивной проверки
def positive_assert(kit_name):
    # В переменную user_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(kit_name)
    # В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert kit_response.json()["name"] == kit_name


# Функция для негативной проверки
def negative_assert_symbol(kit_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(kit_name)

    # В переменную response сохраняется результат
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400


# Функция для негативной проверки - параметр name не передан
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр name состоит из 511 символа
def test_create_kit_511_letter_in_kit_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Ошибка. Параметр name состоит из 0 символов
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_symbol("")


# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_kit_name_get_error_response():
    negative_assert_symbol(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_eng_letter_in_kit_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_ru_letter_in_kit_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_create_kit_simb_letter_in_kit_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание набора. Параметр name с пробелами
def test_create_kit_space_letter_in_kit_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание набора. Параметр name состоит из цифр, переданных строкой
def test_create_kit_digit_letter_in_kit_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Параметр name не передан
def test_create_kit_no_first_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)


# Тест 11. Ошибка. Параметр name передан типом число
def test_create_kit_num_letter_in_kit_name_get_error_response():
    negative_assert_symbol(123)
