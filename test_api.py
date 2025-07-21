import allure
import pytest
import requests
from config import *


@allure.story("API Позитивный")
@allure.title("Поиск фильма по наименованию (кириллица)")
def test_pos_movie_by_cyrillic():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': 'Форрест Гамп'
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie/search?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 200


@allure.story("API Позитивный")
@allure.title("Поиск фильма по наименованию (латиница)")
def test_pos_movie_by_latin():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': 'Forrest Gump'
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie/search?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 200


@allure.story("API Позитивный")
@allure.title("Поиск мультфильмов с рейтингом Кинопоиска (8-10 баллов) 2024 года")
def test_pos_cartoon_by_filter():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 250,
            'selectFields': 'id',
            'selectFields': 'name',
            'selectFields': 'year',
            'selectFields': 'rating',
            'type': 'cartoon',
            'year': '2024',
            'rating.kp': '8-10'
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 200


@allure.story("API Негативный")
@allure.title("Поиск фильма с набором произвольных букв в названии")
def test_neg_movie_by_some_symbols():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': 'qwertyuiop'
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie/search?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 200
    with allure.step("Проверка возврата пустого списка"):
        assert resp.json()["docs"] == []


@allure.story("API Негативный")
@allure.title("Поиск фильма из далекого будущего(2060 год)")
def test_neg_movie_from_future():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'year': 2060
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 400


@allure.story("API Негативный")
@allure.title("Поиск фильма из далекого прошлого (1800 год)")
def test_neg_movie_from_past():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'year': 1800
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 400


@allure.story("API Негативный")
@allure.title("Поиск фильма с неактуальным токеном")
def test_neg_wrong_token():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': 'Форрест Гамп'
        }
    with allure.step("Ввод неактуального значения токена"):
        my_headers = {
            'X-API-KEY': 'REH437Z-2F0MDEN-MTPCCR5'
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie/search?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 401


@allure.story("API Негативный")
@allure.title("Поиск фильма с отсутствующим токеном")
def test_neg_no_token():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': 'Форрест Гамп'
        }
    with allure.step("Отправка запроса"):
        resp = requests.get(
            base_url +
            '/v1.4/movie/search?', params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 401


@allure.story("API Негативный")
@allure.title("Поиск фильма по наименованию (кириллица) с помощью метода PUT")
def test_neg_movie_by_cyrillic_method_put():
    with allure.step("Ввод параметров поиска"):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': 'Форрест Гамп'
        }
    with allure.step("Токен"):
        my_headers = {
            'X-API-KEY': token
        }
    with allure.step("Отправка запроса с методом PUT вместо GET"):
        resp = requests.put(
            base_url +
            '/v1.4/movie/search?', headers=my_headers, params=my_params)
    with allure.step("Проверка статуса кода ответа"):
        assert resp.status_code == 404
