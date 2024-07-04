<p>
  <a href="https://guru.qahacking.ru">
  <picture>
<img alt="Собаседник" src="https://guru.qahacking.ru/templates/yootheme/cache/logosobak-5f874164.png">
    </picture>
  </a>
</p>

<p>
Тест-кейсы для тестового сайта приемника для собак "Собаседник"
</p>

## Используемые инструменты
<div>
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" title="python" alt="python" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" title="pytest" alt="pytest" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184103699-d1b83c07-2d83-4d99-9a1e-83bd89e08117.png" title="selene" alt="selene" width="40" height="40"/>&nbsp
<img src="https://selenoid.autotests.cloud/favicon.ico" title="selenoid" alt="selenoid" width="40" height="40"/>&nbsp
<img src="https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=000000" title="github" alt="github" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png" title="jenkins" alt="jenkins" width="40" height="40"/>&nbsp
<img src="https://camo.githubusercontent.com/501c9d05b6660ba5e1a8753b8461e60d7ff1614656102c254ab800e14a6b19fa/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="40" height="40"/>&nbsp
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
</div>

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


