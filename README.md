# 🚀 Crypto Price Tracker Bot

Telegram-бот для отслеживания цен криптовалют в реальном времени.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Описание

Бот подключается к API криптобиржи и предоставляет актуальную информацию о ценах криптовалют прямо в Telegram.

## ✨ Возможности

- 💰 Получение актуальной цены криптовалюты
- 📊 Поддержка популярных монет (BTC, ETH, SOL и др.)
- 📋 Список доступных криптовалют
- ⚡ Быстрый отклик (данные в реальном времени)
- 🎯 Простой и понятный интерфейс

## 🛠 Технологии

- **Python 3.13**
- **aiogram 3.22.0** - фреймворк для Telegram ботов
- **aiohttp** - асинхронные HTTP запросы к API биржи
- **CoinGecko API** - источник данных

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/zefnn/crypto-price-tracker.git
cd crypto-price-tracker
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `config.py`:
```python
BOT_TOKEN = "your_bot_token_here"
```

5. Запустите бота:
```bash
python bot.py
```

## 🎮 Использование

### Команды:

- `/start` - Начать работу с ботом
- `/help` - Справка по командам
- `/list` - Список доступных криптовалют
- `/price` - Информация о криптовалюте



## 📸 Скриншоты

<img width="1187" height="245" alt="image" src="https://github.com/user-attachments/assets/5bfccee1-9467-4173-84c1-d759a4e4ea5e" />
<img width="1072" height="355" alt="image" src="https://github.com/user-attachments/assets/eb5628d5-1674-4d30-90cb-d96d824b1f8d" />
<img width="1101" height="259" alt="image" src="https://github.com/user-attachments/assets/f4523f85-9b2d-455e-8d56-8d2ef599b944" />
<img width="1202" height="462" alt="image" src="https://github.com/user-attachments/assets/eefb741f-fa6c-423b-b344-9d7de8b03651" />




## 🏗 Архитектура проекта
```
price_crypto_tracker_bot/
├── bot/
│   ├── __init__.py
│   └── handlers.py         # Обработчики команд и сообщений
│
├── services/
│   ├── crypto/
│   │   ├── __init__.py
│   │   └── price_client.py # Клиент для API криптобиржи
│   └── __init__.py
│
├── .env                     # Переменные окружения (токены)
├── .gitignore              # Исключения для Git
├── config.py               # Конфигурация приложения
├── main.py                 # Точка входа в приложение
├── requirements.txt        # Зависимости проекта
└── temp.py                 # Временные тесты/эксперименты
```


### Принципы организации:

✅ **Разделение ответственности** - бизнес-логика отделена от логики бота  
✅ **Модульность** - каждый компонент в своей папке  
✅ **Безопасность** - секретные данные в .env (не в Git)  
✅ **Масштабируемость** - легко добавить новые сервисы или обработчики


## 📈 Планы развития

- [ ] Добавить отслеживание изменения цены (алерты)
- [ ] График изменения цены за период
- [ ] Поддержка нескольких бирж
- [ ] Конвертация в разные фиатные валюты
- [ ] Добавление избранных монет

## 📝 Лицензия

MIT License - можете свободно использовать и модифицировать.

## 👨‍💻 Автор

[Vladislav] - [@vvlaarnb]

---

⭐ Если проект был полезен, поставьте звезду на GitHub!
