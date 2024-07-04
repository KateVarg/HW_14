<p align="center">
  <a href="https://guru.qahacking.ru">
  <picture>
<img alt="Собаседник" src="https://guru.qahacking.ru/templates/yootheme/cache/logosobak-5f874164.png" width="70" height="70">
    </picture>
  </a>
</p>

<p align="center">
Тест-кейсы для тестового сайта приемника для собак "Собаседник"
</p>

## Используемые инструменты
<img title="Python" src="resources/icons/python.svg" height="30" width="30"/> <img title="Jenkins" src="resources/icons/selene.png" height="30" width="30"/>  <img title="Pytest" src="resources/icons/pytest.svg" height="40" width="40"/> <img title="Allure Report" src="resources/icons/allure-report.png" height="40" width="40"/> <img title="Selenoid" src="resources/icons/selenoid.png" height="40" width="40"/> <img title="Jenkins" src="resources/icons/jenkins.svg" height="40" width="40"/> <img title="GitHub" src="resources/icons/github.svg" height="40" width="40"/> <img title="Pycharm" src="resources/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="resources/icons/telegram.png" height="40" width="40"/>

## Запуск

<details><summary>Локально</summary>

<br>1. Склонировать репозиторий:

```
git clone https://github.com/KateVarg/HW_14.git
```

2. Установить зависимости:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Запустить тесты:

```
pytest .
```
</details>

<details><summary>Удалённо</summary>

<br>1. Склонировать репозиторий:

```
git clone https://github.com/KateVarg/HW_14.git
```

2. Установить зависимости:

```
poetry install
```

3. Создать `.env` в корне проекта, внутри него указать:

- **SELENOID_LOGIN**, **SELENOID_PASS**, **SELENOID_URL** — учетные данные и URL для удаленного запуска

4. Запустить тесты:
```
pytest .
```

</details>

## Отчёты

<details><summary>Локально</summary>
<br>

```
allure serve allure-results/
```

В результате:

<img src="resources/allure-report-local.png">


</details>


