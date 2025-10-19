from aiogram import types
from services.crypto.price_client import CryptoPriceClient



# Обработчик команды /start
async def cmd_start(message: types.Message):
    await message.answer("Привет! 👋👋👋\nЯ бот, созданный для получения актуальной цены криптовалюты.\n\n"
                         "Используй /help, чтобы узнать список команд")

# Обработчик команды /help
async def cmd_help(message: types.Message):
    text_help = """
    📋 Доступные команды:
• /start - Начать работу
• /help - Показать справку
• /price [название валюты] - Узнать цену криптовалюты\n(Например <code>/price ethereum</code>)
• /list - Список некоторых криптовалют    
    
Скоро будут добавлены новые функции! 🚀
    """
    await message.answer(text_help)

parser = CryptoPriceClient()

# Обработчик команды /price c аргументами
async def cmd_price(message: types.Message):
    parts = message.text.split()

    coin_id = parts[1].lower() if len(parts) > 1 else 'bitcoin'

    price_data = await parser.get_price(coin_id, 'usd,rub')

    if price_data is None:
        await message.answer("❌ Произошла ошибка при запросе к API. Попробуйте позже.")
    elif not price_data:
        await message.answer(f"❌ Криптовалюта с именем '{coin_id}' не найдена.")
    elif coin_id not in price_data['coin']:
        await message.answer(f"❌ Не удалось получить данные для '{coin_id}'.")
    else:
        usd_price = price_data["price_usd"]
        rub_price = price_data["price_rub"]
        ch_24h = price_data["change_24h"]

        response_text = (
            f"💎 <b>{coin_id.upper()}</b>\n\n"
            f"💵 <b>${usd_price:,.2f}</b>\n"
            f"₽ <b>{rub_price:,.2f}</b>\n"
            f"📊 Изменение за 24ч: <b>{ch_24h:+.2f}%</b>"
        )

        await message.answer(response_text)


# Обработчик сообщений
async def cmd_msg(message: types.Message):
    username = message.from_user.username
    help_text = (
        " я пока понимаю только команды. Вот что я умею:\n"
        "• /start - Начать работу\n"
        "• /help - Показать это сообщение\n"
        "• /list - Список некоторых криптовалют\n"
        "• /price [название валюты] - Узнать цену криптовалюты (например, <code>/price ethereum</code>)"
    )
    await message.answer(username + help_text)

# Обработчик команды /list
async def cmd_list(message: types.Message):
    list_text = (
        "📊 <b>Доступные криптовалюты:</b>\n\n"
        "• Bitcoin (BTC) → <code>/price bitcoin</code>\n"
        "• Ethereum (ETH) → <code>/price ethereum</code>\n"
        "• BNB (BNB) → <code>/price binancecoin</code>\n"
        "• Solana (SOL) → <code>/price solana</code>\n"
        "• XRP (XRP) → <code>/price ripple</code>\n"
        "• Cardano (ADA) → <code>/price cardano</code>\n"
        "• Dogecoin (DOGE) → <code>/price dogecoin</code>\n"
        "• TRON (TRX) → <code>/price tron</code>\n\n"
        "Используй команду <code>/price [id]</code>, чтобы узнать цену."
    )
    await message.answer(list_text)