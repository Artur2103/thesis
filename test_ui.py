import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(1000)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.story("UI")
@allure.title("Проверка открытия раздела Онлайн кинотеатр при нажатии кнопки Онлайн кинотеатр")
def test_button_cinema(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку Онлайн кинотеатр"):
        button_cinema = driver.find_element(
            By.CSS_SELECTOR,
            'a.kinopoisk-header-featured-menu__item[href="https://hd.kinopoisk.ru/"]')
        button_cinema.click()
    with allure.step("проверка на соответствие заголовка страницы Онлайн кинотеатр"):
        current_title = driver.title
        assert current_title == "Онлайн кинотеатр Кинопоиск. Фильмы и сериалы смотреть онлайн в хорошем качестве по подписке"


@allure.story("UI")
@allure.title("Проверка открытия раздела Билеты в кино при нажатии кнопки Билеты в кино")
def test_button_tickets(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку Билеты в кино"):
        button_tickets = driver.find_element(
            By.CSS_SELECTOR,
            'a.kinopoisk-header-featured-menu__item[href*="/lists/movies/movies-in-cinema/"]')
        button_tickets.click()
    with allure.step("Проверка открытия раздела Билеты в кино"):
        current_title = driver.title
        assert current_title == "Билеты в кино — Кинопоиск"


@allure.story("UI")
@allure.title("Проверка открытия раздела Фильмы при нажатии кнопки Фильмы")
def test_button_movie_section(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку Фильмы"):
        button_movie_section = driver.find_element(
            By.CSS_SELECTOR,
            'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="/lists/categories/movies/1/"]')
        button_movie_section.click()
    with allure.step("Проверка открытия раздела Фильмы"):
        current_title = driver.title
        assert current_title == "Смотреть онлайн лучшие фильмы, сериалы и мультфильмы в подборках Кинопоиска в категории “Фильмы“"


@allure.story("UI")
@allure.title("Проверка открытия раздела Сериалы при нажатии кнопки Сериалы")
def test_button_series_section(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку раздела Сериалы"):
        button_series_section = driver.find_element(
            By.CSS_SELECTOR,
            'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="/lists/categories/movies/3/"]')
        button_series_section.click()
    with allure.step("Проверка открытия раздела Сериалы"):
        current_title = driver.title
        assert current_title == "Смотреть онлайн лучшие фильмы, сериалы и мультфильмы в подборках Кинопоиска в категории “Сериалы“"


@allure.story("UI")
@allure.title("Проверка открытия раздела Телеканалы при нажатии кнопки Телеканалы")
def test_button_chanels_section(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку раздела Телеканалы"):
        button_chanels_section = driver.find_element(
            By.CSS_SELECTOR,
            'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="https://hd.kinopoisk.ru/channels"]')
        button_chanels_section.click()
    with allure.step("Проверка открытия раздела Телеканалы"):
        current_title = driver.title
        assert current_title == "Смотреть каналы и ТВ программы онлайн на Кинопоиске"


@allure.story("UI")
@allure.title("Проверка открытия раздела Спорт при нажатии кнопки Спорт")
def test_button_sport_section(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку раздела Спорт"):
        button_sport_section = driver.find_element(
            By.CSS_SELECTOR,
            'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="https://hd.kinopoisk.ru/sport/"]')
        button_sport_section.click()
    with allure.step("Проверка открытия раздела Спорт"):
        current_title = driver.title
        assert current_title == "Смотрите спорт онлайн на Кинопоиске: футбол, хоккей, единоборства в прямом эфире"


@allure.story("UI")
@allure.title("Проверка открытия раздела Медиа при нажатии кнопки Медиа")
def test_button_media_section(driver):
    with allure.step("Открытие главной страницы"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск и клик на кнопку раздела Медиа"):
        button_media_section = driver.find_element(
            By.CSS_SELECTOR,
            'a.styles_root__7mPJN.styles_lightThemeItem__BSbZW[href="/media/"]')
        button_media_section.click()
    with allure.step("Проверка открытия раздела Медиа"):
        current_title = driver.title
        assert current_title == "Медиа на Кинопоиске"
