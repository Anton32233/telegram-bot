# Описание проекта "telegram-bot"
Данный код создан для запуска телеграмм бота, оснавная задача бота, поиск информации о номере сотрудника из таблицы в формате excel.
Бот после того как пользователь вводит команду /stat приветсвует пользователя и говорит о своих возможностях, когда пользователь вводит запрос "Фамилия сотрудника" бот выдает его номер, если человека с такой фамилией нет бот скажет "извините человека с такой фамилей нет"
Этот бот создан на основе библиотеки pyTelegramBotAPI. Ссылка на репозиторий библиотеки: .
## Структура проекта
```text
├── conf.py             - Конфигурационный файл
├── main.py             - Основной скрипт бота
└── search.py           - Файл для поиска данных в Excel
```
