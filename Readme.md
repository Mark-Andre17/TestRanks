### Тестовое задание для Ranks ###
<h2> Описание </h2>
<ul>
  <li> Django Модель Item с полями (name, description, price) </li>
  <li> API с двумя методами:
<strong>GET /buy/{id}</strong>, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
<strong>GET /item/{id}</strong>, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id) </li>
</ul>
  <h2> Залить решение на Github, описать запуск в Readme.md </h2>

<ul>
<li>Клонируйте новый репозиторий себе на компьютер <strong> git clone https://github.com/Mark-Andre17/TestRanks.git </strong>.</li>
<li>Разверните в репозитории виртуальное окружение, в папке скачанного репозитория выполните команду: <strong> python -m venv venv</strong> .</li>
<li>Активируйте виртуальное окружение.</li>
<li>В виртуальном окружении установите зависимости:<strong> pip install -r requirements.txt</strong> .</li>
<li>Создать БД в PostgreSQL либо сменить настройки в файле <strong>settings.py</strong></li>
<li>Перед началом использования сайта необходимо выполнить миграции <strong>(python manage.py migrate)</strong>, создать суперпользователя <strong>(python manage.py createsuperuser)</strong>.</li>
<li>Для запуска сервера введите:<strong> python manage.py runserver</strong>.</li>

<h3>Стек технологий</h3>
asgiref==3.5.2<br>
certifi==2021.10.8<br>
charset-normalizer==2.0.12<br>
Django==4.0.4<br>
djangorestframework==3.13.1<br>
gunicorn==20.1.0<br>
idna==3.3<br>
psycopg2==2.9.3<br>
python-dotenv==0.20.0<br>
pytz==2022.1<br>
requests==2.27.1<br>
sqlparse==0.4.2<br>
stripe==3.0.0<br>
tzdata==2022.1<br>
urllib3==1.26.9
