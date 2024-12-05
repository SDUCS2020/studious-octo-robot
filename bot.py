import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime, timedelta
import re 

API_TOKEN = "7887018266:AAGRbb6aY7zdu8N5Qfs2jEGFj6B8ggdzIm8"
ADMIN_CHANNEL_ID = "-1002426086208" 
CHANNEL_ID_1 = -1002285726390  
CHANNEL_ID_2 = -1002153450146 
CHANNEL_ID_3 = -1001584398072
subscriptions = {}

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)  

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Купить Premium или Premium + КОТ")],
        [KeyboardButton(text="Информация о PREMIUM 🍎")],
        [KeyboardButton(text="Вопрос-Ответ"), KeyboardButton(text="Отзывы")],
        [KeyboardButton(text="Написать в поддержку")],
    ],
    resize_keyboard=True
)

info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Купить Premium или Premium + КОТ")],
        [KeyboardButton(text="Загрузить скриншот")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)

qa_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Смогу ли я быть уверена, что делаю самомассаж или тейпирование правильно и не принесу вред?")],
        [KeyboardButton(text="Вы сможете помочь проверить состав средства или правильность выбора моего домашнего ухода?")],
        [KeyboardButton(text="Зачем мне брать Молодильный бот PREMIUM и тренировки йога в клубе КОТ?")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в Молодильный бот! Выберите действие:", reply_markup=main_menu)

@router.message(lambda message: message.text == "🍎Купить PREMIUM в Молодильном боте🍎")
async def premium_info(message: types.Message):
    await message.answer("Выберите, что вас интересует нажав на кнопку👇", reply_markup=info_menu)

@router.message(lambda message: message.text == "Написать в поддержку")
async def premium_info(message: types.Message):
     text = (
        "Ддя получения поддержки напишите👇:\n\n"
        "@poddergkako\n\n"
     )

     await message.answer(text)

@router.message(lambda message: message.text == "Купить Premium или Premium + КОТ")
async def payment_info(message: types.Message):
    text = (
        "1. Выбирайте период подписки и оплачивайте соответствующую сумму\n\n"
        "Тарифы на PREMIUM-доступ в Молодильный бот🍎:\n\n"
        "1 месяц: 10$ — 34,8 BYN / 27,5 GEL\n"
        "3 месяца: 27$ — 93 BYN / 75 GEL\n"
        "6 месяцев: 50$ — 174 BYN / 138 GEL\n"
        "12 месяцев: 90$ — 313 BYN / 248 GEL\n\n"
        "Пакеты PREMIUM Молодильный бот🍎 + Клуб КОТ:\n\n"
        "1 месяц: 15$ — 52 BYN / 41,2 GEL\n"
        "3 месяца: 39$ — 136 BYN / 108 GEL\n"
        "6 месяцев: 80$ — 279 BYN / 220 GEL\n"
        "12 месяцев: 160$ — 556,8 BYN / 440 GEL\n\n"
        "2. Оплачивайте по реквизитам\n\n"
        "🇧🇾Беларусь:\n"
        "1️⃣ ЕРИП: Банковские и финансовые услуги → Банки НКФО → Альфа-Банк → 375256719780\n"
        "2️⃣ С Альфа-Банк Беларуси по номеру телефона: 375256719780\n"
        "3️⃣ По номеру карты: 9112 3880 0196 1148 (Ivan Karalko)\n\n"
        "🌍 Для других стран:\n"
        "1️⃣ Банковская карта Грузии (TBC): 4315 7140 1661 1277 (Ivan Karalko)\n"
        "IBAN: GE92TB7398345064400010\n\n"
        "💹 Крипта:\n"
        "USDT (TRC-20): TYnFwyLqhxfrwgjNpw5A9ANXKpLLCtcQYm\n"
        "Bybit UID: 15786723\n\n"
        "3. 📤 После оплаты нажмите на \"Загрузить скриншот\" и отправьте скриншот.\n"
        "Доступ открывается сразу или до 3 часов после."
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Загрузить скриншот", callback_data="upload_screenshot")],
            [InlineKeyboardButton(text="Закрыть", callback_data="close")]
        ]
    )

    await message.answer(text, reply_markup=keyboard)

@router.callback_query(lambda callback: callback.data == "upload_screenshot")
async def handle_upload_screenshot(callback: CallbackQuery):
    await callback.message.answer("Пожалуйста, загрузите скриншот.")
    await callback.answer()

@router.callback_query(lambda callback: callback.data == "close")
async def handle_close(callback: CallbackQuery):
    await callback.message.delete()  
    await callback.answer()  

@router.message(lambda message: message.text == "Вопрос-Ответ")
async def faq(message: types.Message):
    await message.answer("Выберите вопрос:", reply_markup=qa_menu)

@router.message(lambda message: message.text == "Смогу ли я быть уверена, что делаю самомассаж или тейпирование правильно и не принесу вред?")
async def qa_1(message: types.Message):
    text = (
        "Вы точно не навредите себе и будете выполнять технику правильно, потому что все уроки записаны "
        "качественно и подробно. Вы также сможете снять видео и отправить его в чат со мной, чтобы я "
        "лично проверил технику. Это касается и тейпирования."
    )
    await message.answer(text)

@router.message(lambda message: message.text == "Вы сможете помочь проверить состав средства или правильность выбора моего домашнего ухода?")
async def qa_2(message: types.Message):
    text = (
        "Да, Иван лично будет в Telegram-чате, где вы сможете задать любой вопрос и быть уверены, что "
        "все делаете правильно."
    )
    await message.answer(text)

@router.message(lambda message: message.text == "Зачем мне брать Молодильный бот PREMIUM и тренировки йога в клубе КОТ?")
async def qa_3(message: types.Message):
    text = (
        "Работа с возрастными изменениями — это не только уход за лицом, но и проработка всего тела. "
        "Каждый знает, что для хорошего самочувствия и фигуры важно заниматься спортом. "
        "Раньше я ходил в тренажерный зал, но однажды попробовал йогу с Сабиной (тренером клуба КОТ и моей женой) — "
        "теперь я тренируюсь только по ее урокам. Клуб КОТ полностью решает вопрос занятий спортом: все, что вам нужно, "
        "— это коврик, 20–60 минут времени и всего 10$ в месяц."
    )
    await message.answer(text)

@router.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    await message.answer("Возвращаемся в главное меню:", reply_markup=main_menu)

premium_club_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="PREMIUM-доступ 🍎")],
        [KeyboardButton(text="Клуб КОТ 🌰")],
        [KeyboardButton(text="Стоимость/оплата")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)

@router.message(lambda message: message.text == "Информация о PREMIUM 🍎")
async def buy_premium(message: types.Message):
    await message.answer(
        "Выберите раздел:",
        reply_markup=premium_club_menu
    )

@router.message(lambda message: message.text == "PREMIUM-доступ 🍎")
async def premium_access(message: types.Message):
    text = (
        "За 10$ в месяц вы получаете:\n"
        " • Курс Instaskin (20+ уроков): подбор ухода, эффективный самомассаж, техники буккального массажа и гуаша.\n"
        " • Курс самотейпирования: борьба с возрастными изменениями и спазмами мышц.\n"
        " • Чат для консультаций где отвечает лично Иван Королько: помогает в подборе средств, проверяет выполнение техник самомассажа или тейпирования.\n\n"
        "При оплате на более долгий срок ещё выгоднее👍🏽\n"
        "1 месяц: 10$ — 34,8 BYN / 27,5 GEL\n"
        "3 месяца: 27$ — 93 BYN / 75 GEL\n"
        "6 месяцев: 50$ — 174 BYN / 138 GEL\n"
        "12 месяцев: 90$ — 313 BYN / 248 GEL\n\n"
        "Специальные условия, если приобретаете с PREMIUM ещё клуб КОТ, с тренировками силовой йоги. Подробнее про КОТ по кнопке ниже👇:\n\n"
        "Пакеты PREMIUM Молодильный бот🍎 + Клуб КОТ:\n\n"
        "1 месяц: 15$ — 52 BYN / 41,2 GEL\n"
        "3 месяца: 39$ — 136 BYN / 108 GEL\n"
        "6 месяцев: 80$ — 279 BYN / 220 GEL\n"
        "12 месяцев: 160$ — 556,8 BYN / 440 GEL\n"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подробнее про КОТ", callback_data="kot_club")],
            [InlineKeyboardButton(text="Оплатить", callback_data="payment")]
        ]
    )

    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

@router.callback_query(lambda callback: callback.data == "kot_club")
async def kot_club_handler(callback: types.CallbackQuery):
    text = (
        "Клуб КОТ - это телеграм-канал для тренировок на все тело и лекциями про здоровье и питание. КОТ закроет все твои потребности в физической нагрузке для того чтобы иметь сексуальное и здоровое тело в любом возрасте, восстановить осанку и приобрести гораздо более высокое качество жизни.\n"
        "Что входит?\n"
        "• 3 силовые йоги в неделю в прямом эфире.\n"
        "• Записи всех тренировок остаются навсегда в канале. Там уже более 73! тренировок где вы можете выбрать продолжительность (15, 40, 60, 80 минут), а также уровни сложности и акцент на ноги, попу и проч.\n"
        "• Еженедельные короткие практики (15–20 мин).\n"
        "• Лекции: питание, похудение, рецепты, добавки.\n"
        "• Разбор анализов раз в месяц.\n"
        "• Комьюнити женщин с 🔥 энергией.\n"
        "Тренировки проводит самый мощный и мотивирующий тренер у которого я сам занимаюсь - Сабина🔥\n\n"

        "Тарифы на PREMIUM молодильного бота🍎 + клуб КОТ\n\n"

        "1 месяц: 15$ — 52 BYN / 41,2 GEL\n"
        "3 месяца: 39$ — 136 BYN / 108 GEL\n"
        "6 месяцев: 80$ — 279 BYN / 220 GEL\n"
        "12 месяцев: 160$ — 556,8 BYN / 440 GEL\n"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Оплатить", callback_data="payment")]
        ]
    )

    await callback.message.answer(text, reply_markup=keyboard)

@router.callback_query(lambda callback: callback.data == "payment")
async def handle_payment(callback: CallbackQuery):
    text = (
        "1. Выбирайте период подписки и оплачивайте соответствующую сумму\n\n"
        "Тарифы на PREMIUM-доступ в Молодильный бот🍎:\n\n"
        "1 месяц: 10$ — 34,8 BYN / 27,5 GEL\n"
        "3 месяца: 27$ — 93 BYN / 75 GEL\n"
        "6 месяцев: 50$ — 174 BYN / 138 GEL\n"
        "12 месяцев: 90$ — 313 BYN / 248 GEL\n\n"
        "Пакеты PREMIUM Молодильный бот🍎 + Клуб КОТ:\n\n"
        "1 месяц: 15$ — 52 BYN / 41,2 GEL\n"
        "3 месяца: 39$ — 136 BYN / 108 GEL\n"
        "6 месяцев: 80$ — 279 BYN / 220 GEL\n"
        "12 месяцев: 160$ — 556,8 BYN / 440 GEL\n\n"
        "2. Оплачивайте по реквизитам\n\n"
        "🇧🇾Беларусь:\n"
        "1️⃣ ЕРИП: Банковские и финансовые услуги → Банки НКФО → Альфа-Банк → 375256719780\n"
        "2️⃣ С Альфа-Банк Беларуси по номеру телефона: 375256719780\n"
        "3️⃣ По номеру карты: 9112 3880 0196 1148 (Ivan Karalko)\n\n"
        "🌍 Для других стран:\n"
        "1️⃣ Банковская карта Грузии (TBC): 4315 7140 1661 1277 (Ivan Karalko)\n"
        "IBAN: GE92TB7398345064400010\n\n"
        "💹 Крипта:\n"
        "USDT (TRC-20): TYnFwyLqhxfrwgjNpw5A9ANXKpLLCtcQYm\n"
        "Bybit UID: 15786723\n\n"
        "3. 📤 После оплаты нажмите на \"Загрузить скриншот\" и отправьте скриншот.\n"
        "Доступ открывается сразу или до 3 часов после."
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Загрузить скриншот", callback_data="upload_screenshot")],
            [InlineKeyboardButton(text="Закрыть", callback_data="close")]
        ]
    )

    await callback.message.answer(text, reply_markup=keyboard)

@router.message(lambda message: message.text == "Клуб КОТ 🌰")
async def club_kot(message: types.Message):
    text = (
        "Клуб КОТ - это телеграм-канал для тренировок на все тело и лекциями про здоровье и питание. КОТ закроет все твои потребности в физической нагрузке для того чтобы иметь сексуальное и здоровое тело в любом возрасте, восстановить осанку и приобрести гораздо более высокое качество жизни.\n"
        "Что входит?\n"
        "• 3 силовые йоги в неделю в прямом эфире.\n"
        "• Записи всех тренировок остаются навсегда в канале. Там уже более 73! тренировок где вы можете выбрать продолжительность (15, 40, 60, 80 минут), а также уровни сложности и акцент на ноги, попу и проч.\n"
        "• Еженедельные короткие практики (15–20 мин).\n"
        "• Лекции: питание, похудение, рецепты, добавки.\n"
        "• Разбор анализов раз в месяц.\n"
        "• Комьюнити женщин с 🔥 энергией.\n"
        "Тренировки проводит самый мощный и мотивирующий тренер у которого я сам занимаюсь - Сабина🔥\n\n"

        "Тарифы на PREMIUM молодильного бота🍎 + клуб КОТ\n\n"

        "1 месяц: 15$ — 52 BYN / 41,2 GEL\n"
        "3 месяца: 39$ — 136 BYN / 108 GEL\n"
        "6 месяцев: 80$ — 279 BYN / 220 GEL\n"
        "12 месяцев: 160$ — 556,8 BYN / 440 GEL\n"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Оплатить", callback_data="payment")]
        ]
    )

    await message.answer(text, reply_markup=keyboard)

@router.message(lambda message: message.text == "Стоимость/оплата")
async def payment_info(message: types.Message):
    text = (
        "1. Выбирайте период подписки и оплачивайте соответствующую сумму\n\n"
        "Тарифы на PREMIUM-доступ в Молодильный бот🍎:\n\n"
        "1 месяц: 10$ — 34,8 BYN / 27,5 GEL\n"
        "3 месяца: 27$ — 93 BYN / 75 GEL\n"
        "6 месяцев: 50$ — 174 BYN / 138 GEL\n"
        "12 месяцев: 90$ — 313 BYN / 248 GEL\n\n"
        "Пакеты PREMIUM Молодильный бот🍎 + Клуб КОТ:\n\n"
        "1 месяц: 15$ — 52 BYN / 41,2 GEL\n"
        "3 месяца: 39$ — 136 BYN / 108 GEL\n"
        "6 месяцев: 80$ — 279 BYN / 220 GEL\n"
        "12 месяцев: 160$ — 556,8 BYN / 440 GEL\n\n"
        "2. Оплачивайте по реквизитам\n\n"
        "🇧🇾Беларусь:\n"
        "1️⃣ ЕРИП: Банковские и финансовые услуги → Банки НКФО → Альфа-Банк → 375256719780\n"
        "2️⃣ С Альфа-Банк Беларуси по номеру телефона: 375256719780\n"
        "3️⃣ По номеру карты: 9112 3880 0196 1148 (Ivan Karalko)\n\n"
        "🌍 Для других стран:\n"
        "1️⃣ Банковская карта Грузии (TBC): 4315 7140 1661 1277 (Ivan Karalko)\n"
        "IBAN: GE92TB7398345064400010\n\n"
        "💹 Крипта:\n"
        "USDT (TRC-20): TYnFwyLqhxfrwgjNpw5A9ANXKpLLCtcQYm\n"
        "Bybit UID: 15786723\n\n"
        "3. 📤 После оплаты нажмите на \"Загрузить скриншот\" и отправьте скриншот.\n"
        "Доступ открывается сразу или до 3 часов после."
        "⚠️Если нужна помощь - пиши нам в поддержку @poddergkako ⚠️"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Загрузить скриншот", callback_data="upload_screenshot")],
            [InlineKeyboardButton(text="Закрыть", callback_data="close")]
        ]
    )

    await message.answer(text, reply_markup=keyboard)

@router.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    await message.answer("Возвращаемся в главное меню:", reply_markup=main_menu)

@router.message(lambda message: message.text == "Загрузить скриншот")
async def upload_screenshot(message: types.Message):
    await message.answer("Отправьте скриншот оплаты для подтверждения:")

@router.message(lambda message: message.text == "Отзывы")
async def upload_screenshot(message: types.Message):
    text = (
        "🙏🏼Отзывы обо мне как о специалисте можно посмотреть в актуальном с названием \"ОТЗЫВЫ\" в моем Инстаграм по ссылке: \n\n" 
        "https://www.instagram.com/cosmetic.man/"
    )
    await message.answer(text)

@router.message(F.photo)
async def handle_photo(message: types.Message):
    user_id = message.from_user.id
    photo_id = message.photo[-1].file_id

    await message.bot.send_message(
        ADMIN_CHANNEL_ID,
        f"Новая заявка на подписку от пользователя:\n\n"
        f"Имя: {message.from_user.full_name}\n"
        f"ID: {user_id}\n\n"
    )
    await message.bot.send_photo(ADMIN_CHANNEL_ID, photo=photo_id)

    await message.answer("Данные успешно отправлены. После проверки доступ открывается мгновенно или в течение 3 часов.")

    durations = [
        ("PR 1 мес", "sub_1_month"),
        ("PR 3 мес", "sub_3_months"),
        ("PR 6 мес", "sub_6_months"),
        ("PR 12 мес", "sub_12_months"),
        ("PR+КОТ 1 мес", "sub_1_month_cat"),
        ("PR+КОТ 3 мес", "sub_3_months_cat"),
        ("PR+КОТ 6 мес", "sub_6_months_cat"),
        ("PR+КОТ 12 мес", "sub_12_months_cat"),
    ]

    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=durations[i][0], callback_data=f"{durations[i][1]}:{user_id}"),
            InlineKeyboardButton(text=durations[i + 1][0], callback_data=f"{durations[i + 1][1]}:{user_id}")
        ]
        for i in range(0, len(durations), 2) 
        ]
    )

    await message.bot.send_message(ADMIN_CHANNEL_ID, "Выберите вариант подписки:", reply_markup=keyboard)

@router.callback_query(lambda c: c.message.chat.id == int(ADMIN_CHANNEL_ID))
async def handle_subscription_choice(callback: CallbackQuery):
    data = callback.data.split(":") 
    choice, user_id = data[0], int(data[1]) 

    durations = {
        "sub_1_month": 30,
        "sub_3_months": 90,
        "sub_6_months": 180,
        "sub_12_months": 365,
        "sub_1_month_cat": 30,
        "sub_3_months_cat": 90,
        "sub_6_months_cat": 180,
        "sub_12_months_cat": 365
    }
    days = durations.get(choice, 30)
    expiration_date = datetime.now() + timedelta(days=days)

    subscriptions[user_id] = expiration_date

    if "cat" in choice: 
        is_cat_subscriber = True
        channel_ids = [CHANNEL_ID_1, CHANNEL_ID_3, CHANNEL_ID_2]
        channel_descriptions = [
            "1️⃣Курс \"эстетическое тейпирование\"",
            "2️⃣Курс INSTASKIN с самомассажами и исчерпывающей информацией о том как правильно выбрать и пользоваться домашним уходом",
            "4️⃣Клуб КОТ с тренировками"
        ]
    else:
        is_cat_subscriber = False
        channel_ids = [CHANNEL_ID_1, CHANNEL_ID_3]
        channel_descriptions = [
            "1️⃣Курс \"эстетическое тейпирование\"",
            "2️⃣Курс INSTASKIN с самомассажами и исчерпывающей информацией о том как правильно выбрать и пользоваться домашним уходом"
        ]

    invite_links = []
    for channel_id in channel_ids:
        invite_link = await generate_invite_link(channel_id)
        invite_links.append(invite_link)

    static_text = "3️⃣Чат для обратной связи и помощи в освоении информации с Королько Иваном - https://t.me/+4Lby-7srbjBhOGMy"

    invite_links_text = "\n".join(
        [f"{desc} - {link}" for desc, link in zip(channel_descriptions, invite_links[:2])]
    )
    invite_links_text += f"\n{static_text}\n"
    invite_links_text += "\n".join(
        [f"{desc} - {link}" for desc, link in zip(channel_descriptions[2:], invite_links[2:])]
    )

    await callback.bot.send_message(
        user_id,
        f"Ваша подписка активирована до {expiration_date.strftime('%d.%m.%Y')}.\n"
        f"Вот ваши ссылки для доступа. Подпишитесь на все:\n"
        f"{invite_links_text}"
    )

    await callback.message.answer(f"Подписка на {days} дней успешно активирована для пользователя {user_id}.")

    await callback.message.edit_reply_markup(reply_markup=None)

    asyncio.create_task(schedule_reminders_and_removal(user_id, expiration_date, is_cat_subscriber))

    await callback.answer("Подписка активирована.")

async def schedule_reminders_and_removal(user_id, expiration_date, is_cat_subscriber=False):
    """
    Устанавливает напоминания и удаляет пользователя из группы после истечения подписки.
    :param user_id: ID пользователя
    :param expiration_date: Дата истечения подписки
    :param is_cat_subscriber: Подписка на КОТ (True) или обычная (False)
    """
    reminders = [5, 3, 1] 
    for days_before in reminders:
        reminder_time = expiration_date - timedelta(days=days_before)
        wait_time = (reminder_time - datetime.now()).total_seconds()
        if wait_time > 0:
            await asyncio.sleep(wait_time)
            await bot.send_message(
                user_id,
                f"Напоминание: Ваша подписка истекает через {days_before} день(дней). Нажмите 'Оплата' для продления.",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[[KeyboardButton(text="Оплата")]],
                    resize_keyboard=True
                )
            )

    wait_time = (expiration_date - datetime.now()).total_seconds()
    if wait_time > 0:
        await asyncio.sleep(wait_time)

    channels_to_remove = [CHANNEL_ID_1, CHANNEL_ID_2, CHANNEL_ID_3] if is_cat_subscriber else [CHANNEL_ID_1, CHANNEL_ID_3]
    for channel_id in channels_to_remove:
        try:
            await bot.kick_chat_member(chat_id=channel_id, user_id=user_id)
            await bot.send_message(user_id, f"Вы были удалены из группы {channel_id} из-за истечения подписки.")
        except Exception as e:
            print(f"Ошибка при удалении пользователя {user_id} из канала {channel_id}: {e}")

async def generate_invite_link(channel_id: int):
    invite_link = await bot.create_chat_invite_link(chat_id=channel_id, member_limit=1)  
    return invite_link.invite_link

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
