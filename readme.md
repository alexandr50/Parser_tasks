<h3>Проект парсер задач с сайта codeforses.com</h3>

- Класс EngineCF парсит сайт codeforses.com
- Класс DBManager работает с бд
- В файле telegram_bot.py происходит работа в ботом

1. Скачайте себе проект на локальную машину командой git clone ...
2. Перейдите в корень проекта в папку Parser_tasks
3. Установите зависимости командой pip install -r requirements.txt
4. Запустите файл run.py
5. После запуска в телеграмме доступен бот https://t.me/TasksCodeforsesBot
6. Команда /theme открывает меню по сортировке задач по теме  
7. Команда /rating открывает меню по сортировке задач по рейтингу
8. Для запуска крон задачи наберите в терминале в корневой папке пректа команду python schedule.py
9. Крон задача проверяет каждый час не появилось ли новой записи на сайте и если это так до бобавляе в бд
10. Запуск тестов командой coverage run -m unittest discover
11. Посмотреть покрытие тестами coverage run -m unittest discover
