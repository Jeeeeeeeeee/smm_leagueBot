#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
doc string goes here
"""

__all__ = ['']

# Standard library imports.
import logging
import telebot
import config
import types
import pytz
import datetime, time
import schedule

# Related third party imports.


# Local application/library specific imports.

# Create your models here.
P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)

logger = telebot.logger
logging.basicConfig(filename='../SMM_LeagueBot/log_bot.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('🎓 О мастер-классе', '👩‍🏫 Об Эксперте')
    keyboard.row('🎁 Как получить бонус', '📱 Связаться с нами')
    keyboard.row('🔐 Закрытая группа мастер-класса')
    bot.send_message(
        message.chat.id,
        '😍УРААААА! Рада приветсвовать тебя на своем 2-х дневном БЕСПЛАТНОЙ МАСТЕР-КЛАССЕ:\n' +
        '<b>"КАК ЗА 5 ШАГОВ ОБУЧИТЬСЯ ПРОДВИЖЕНИЮ В ИНСТАГРАМ И ПЕРЕЙТИ НА УРОВЕНЬ ДОХОДА ОТ 1000$"</b>🤑\n\n' +
        '👍24, 26 августа я в прямом эфире поделюсь с тобой методиками и техниками по продвижению в инстаграм, а так же расскажу КАК ЗАРАБАТЫВАТЬ ОТ 1000$ только благодаря тебефону.\n\n' +
        'Вся основная коммуникация пройдет в нашей закрытой группе. Так же для тебя будет <b>БОНУС</b>, для этого тебе нужно перейти в группу инстаграм и написать в ДИРЕКТ слово <b>"БОНУС"</b> и я с удовольствием отправлю его тебе!\n\n' +
        'Чтобы ты успел приссоедениться к нашей закрытой группе, нажми здесь кнопку "перейти в группу" под этим смс и моя помощница одобрит твою заявку ↘\n\n' +
        'Я создала максимально комфортные условия для тебя и жду тебя на прямом эфире уже <b>24 и 26 АВГУСТА.</b>\n\n' +
        '🔥ЭТО БУДЕТ 2 МОЩНЫХ ДНЯ!🔥\n\n До встречи, скорее переходи в группу\n\n' +
        '⏭ <a href="https://instagram.com/smm.league?igshid=1q2864gggcbhz"><b>ССЫЛКА НА ГРУППУ ЗДЕСЬ</b></a> ⏪\n\n',
        reply_markup=keyboard,
        parse_mode='HTML',
    )

    def august_20():
        bot.send_message(message.from_user.id, '🤩Привет, мой инстаграм герой.\n\n' +
                         'Я волнусь за тебя, поэтому решила продублировать ссылку на закрытую группу, чтобы ты не пропустил все полезности и ПОДАРОК, который ждет тебя в ДИРЕКТ.🎁\n\n' +
                         '✅ Перейди по ссылке под эфим смс\n' +
                         '✅ Когда твою заявку одобрит администратор, напиши в директ слово "БОНУС"\n\n' +
                         'Я не позволю тебе остаться без подарка, поэтому жду тебя там.\n\n' +
                         '🌟До встречи на эфирах 24 августа в 19:30 и 26 августа в 20:00.\n\n' +
                         'С любовью и обнимашками, твоя Малинка🎁', parse_mode='HTML')

    def august_23():
        bot.send_message(message.from_user.id, '🌟Уже завтра 24 августа в 19:30 Киев/МСК мы начинаем!\n\n' +
                         '🎓Первый эфир нашего бесплатного мастер-класса <b>"КАК ЗА 5 ШАГОВ ОБУЧИТЬСЯ ПРОДВИЖЕНИЮ В ИНСТАГРАМ И ПЕРЕЙТИ НА УРОВЕНЬ ДОХОДА ОТ 1000$"</b>🤑\n\n' +
                         'Отложи все свои дела и готовься быть online в это время, я тебя жду!\n' +
                         'До встречи уже завтра.❤️', parse_mode='HTML')

    def august_24():
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Я БУДУ!",
                                                        url="https://start.bizon365.ru/room/55364/smmleague_webinar")
        keyboard.add(url_button)
        bot.send_message(message.from_user.id, '🎉УРААА, сегодня в 19:30 мы начинаем!\n\n' +
                         'С тобой на связи Алексия Малинова!\n' +
                         'Приготовься, возьми листик и ручку информации и полезностей будет много!\n\n' +
                         '<i>6 навыков, которые ты получишь сегодня 24 АВГУСТА В 19:30:</i>\n\n' +
                         '1️⃣ Узнаешь как работает воронка продаж в инстаграм, которая приносит регулярный доход\n' +
                         '2️⃣ Оформишь продающую шапку профиля ШАПКУ ПРОФИЛЯ и поймешь как создать свой мини-сайт\n' +
                         '3️⃣ Научишься создавать контент, который вовлекает людей\n' +
                         '4️⃣ Усвоишь главные ошибки, которые допускают неопытные специалисты\n' +
                         '5️⃣ Поймешь как грамотно управлять всеми инструментами продвижения\n' +
                         '6️⃣ <b>УЗНАЕШЬ КАК НАЧАТЬ ЗАРАБАТЫВАТЬ ОТ 1000$ ТОЛЬКО БЛАГОДАРЯ ТЕЛЕФОНУ</b>\n' +
                         '7️⃣ Я расскажу про курс-практикум "Голая правда SMM"\n' +
                         '6️⃣Вот твоя ссылка на вебинарную комнату, подключайся в 19:30 и не опаздывай, чтобы не пропустить ничего важного!\n\n' +
                         'Перейди сейчас по этой ссылке и нажми "Я буду", чтобы занять за собой место, так как колличество мест ограничено, успей забрать своё.',
                         reply_markup=keyboard, parse_mode='HTML')

    def august_24_19():
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="СМОТРЕТЬ ВЕБИНАР!",
                                                        url="https://start.bizon365.ru/room/55364/smmleague_webinar")
        keyboard.add(url_button)
        bot.send_message(message.from_user.id, 'С тобой на связи Алексия Малинова!\n' +
                         '🔥Приготовься, мы начинаем через 10 минут!\n\n',
                         reply_markup=keyboard, parse_mode='HTML')

    def august_25():
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="ПЕРЕЙТИ НА ВЕБИНАР",
                                                        url="https://start.bizon365.ru/room/55364/smmleague_webinar")
        keyboard.add(url_button)
        bot.send_message(message.from_user.id, '😊Добрый день, мой дорогой Инста-герой.\n\n' +
                         '🎉Как твое настроение сегодня?\n' +
                         'Вчера состоялся главный прямой эфир, но многие писали, что не смогли быть онлайн и пропустили трансляцию.\n\n' +
                         '✅Я РЕШИЛА ПРОВЕСТИ ПОВТОР этого эфира и жду тебя сегодня 25 августа в 19:30.\n\n' +
                         'Не пропусти сегодня, так какк это твоя последняя возможность посмотреть трансляцию БЕСПЛАТНО.\n' +
                         '❗️Напоминаю! В вебинарной комнате комнате количество мест ограничено, поэтому обязательно приходи,если вчера не получилось, либо появились какие-то вопросы.\n\n' +
                         'Записи и повтора больше не будет ‼️\n' +
                         '✅ Жмите на кнопку ниже', reply_markup=keyboard, parse_mode='HTML')

    def august_26():
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Я БУДУ!",
                                                        url="https://start.bizon365.ru/room/55364/smmleague_webinar")
        keyboard.add(url_button)
        bot.send_message(message.from_user.id, '❤️Привет герой!\n\n' +
                         '🎉Сегодня состоится наша финальная встреча.\n\n' +
                         '⏰Ровно в 20:00, сегодня, 26 августа – я проведу сессию ответов на ваши вопросы\n' +
                         'Готовься рассказать о своих трудностях, так как я их решу!\n\n' +
                         '❗️Напоминаю! В вебинарной комнате комнате количество мест ограничено, перейди по ссылке и напиши в чате "я буду", чтобы занять за собой место.\n\n' +
                         '👇Жми на ссылку скореееееей👇', reply_markup=keyboard, parse_mode='HTML')

    # sleep until 20AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, 20, 10, 0)
    time.sleep((future - t).seconds)
    august_20()

    # sleep until 23AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, 23, 10, 0)
    time.sleep((future - t).seconds)
    august_23()

    # sleep until 24AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, 24, 10, 0)
    time.sleep((future - t).seconds)
    august_24()

    # sleep until 24 19:20AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, 24, 19, 20)
    time.sleep((future - t).seconds)
    august_24_19()

    # sleep until 25AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, 25, 10, 0)
    time.sleep((future - t).seconds)
    august_25()

    # sleep until 26AM
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, 26, 10, 0)
    time.sleep((future - t).seconds)
    august_26()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🎓 О мастер-классе':
        bot.send_message(message.from_user.id,
                         '❗<b>Бесплатный 2-х дневный мастер-класс по продвижению в Instagram.</b>❗️\n\n' +
                         '🤑<b>"КАК ЗА 5 ШАГОВ ОБУЧИТЬСЯ ПРОДВИЖЕНИЮ В ИНСТАГРАМ И ПЕРЕЙТИ НА УРОВЕНЬ ДОХОДА ОТ 1000$"</b>🤑️\n\n' +
                         '<b>ДАТЫ МАСТЕР КЛАССА:</b>\n' +
                         '⏰24 августа 19:30 Киев/МСК – ГЛАВНЫЙ ПРЯМОЙ ЭФИР\n' +
                         '⏰26 августа 20:00 Киев/МСК – КОУЧИНГОВАЯ СЕССИЯ ВОПРОС-ОТВЕТ\n\n' +
                         'СРОЧНО! Вся основная коммуникация будет проходить в нашей закрытой группе, вот твоя персональная ссылка, скорее переходи и забери свой бонус за регистрацию!\n\n' +
                         '⏭ <a href="https://instagram.com/smm.league?igshid=1q2864gggcbhz"><b>ССЫЛКА НА ГРУППУ ЗДЕСЬ</b></a> ⏪\n\n' +
                         '_________________________________________________________________________\n\n' +
                         '<b>6 навыков</b>, которые ты получишь, КОТОРЫЕ ТЫ ПОЛУЧИШЬ <b>24 АВГУСТА В 19:30:</b>\n\n' +
                         '1️⃣ Узнаешь как работает воронка продаж в инстаграм, которая приносит регулярный доход\n' +
                         '2️⃣ Оформишь продающую шапку профиля ШАПКУ ПРОФИЛЯ и поймешь как создать свой мини-сайт\n' +
                         '3️⃣ Научишься создавать контент, который вовлекает людей\n' +
                         '4️⃣ Усвоишь главные ошибки, которые допускают неопытные специалисты\n' +
                         '5️⃣ Поймешь как грамотно управлять всеми инструментами продвижения\n' +
                         '6️⃣ <b>УЗНАЕШЬ КАК НАЧАТЬ ЗАРАБАТЫВАТЬ ОТ 1000$ ТОЛЬКО БЛАГОДАРЯ ТЕЛЕФОНУ</b>\n' +
                         '7️⃣ Я расскажу про курс-практикум "Голая правда SMM" \n\n' +
                         '<b>26 августа в 20:00</b> я проведу сессию ответов на ваши вопросы, где мы поговорим о трудностях связанных с продвижением в Instagram и зададите свой главный вопрос.\n\n' +
                         '<b>ВАЖНО:\n На эфирах 24, 26 августа присутствовать онлайн</b>, так как вся жара будет в прямом эфире и это единственная возможность получиться это информацию бесплатно, так как запись эфира будет платной.\n\n' +
                         '🎯Знай, ты находишься в числе 8% тех людей, которые готовы действовать и развиваться! SMM специалист - это профессия будущего, которая всегда будет радовать творческой атмосферой и постоянным высоким заработков. Я жду тебя в эфире, чтобы научить главным фишкам продвижения и помочь освоить Инстаграм.\n\n' +
                         'Я верю в тебя и до встречи!\n С любовью и обнимашками, твоя Малинка❤️',
                         parse_mode='HTML')

    elif message.text == '👩‍🏫 Об Эксперте':
        bot.send_message(message.from_user.id, '🌟ПРИВЕЕЕЕЕЕЕЕЕЕТ мой милый инста-друг!🤩\n\n' +
                         'Меня зовут Алексия Малинова и я рада видеть тебя в числе счастливчиков, которые будут на моем мастер-классе.\n\n' +
                         'Сейчас я хочу рассказать тебе немного о себе, чтобы ты понимал кто с тобой на связи и с чего вдруг я тут умничаю.\n\n' +
                         'Сразу хочу поделиться информацией о своем образовании:\n\n' +
                         '👩‍🎓<b>Образование:</b>\n\n' +
                         '👉 Высшее: Славянская филология. Журналистика\n' +
                         '👉 Digital marketing institute\n' +
                         '👉 Международная школа SMM\n' +
                         '👉 Курс "Основы копирайтинга"\n' +
                         '👉 Более 100 тренингов по продвижению в соц. сетях\n' +
                         '👉 3500$ потратила на свое образование\n' +
                         '👉 Более 300 консультаций\n' +
                         '👉 Воронка продаж в Stories\n' +
                         '👉 Построение конверсионной воронки Landing Page\n' +
                         '👉 Тренды визуала в Инстаграм в 2020\n' +
                         '👉 Ораторское искусство. Искусство речи.\n\n' +
                         'Мой путь в SMM начался 2 с половиной года назад, когда я пошла учиться в свою первую школу SMM. Я была растерянной студенткой, которая закончила университет, получила диплом журналиста и с огромными амбициями и рвением пошла искать работу, но куда бы я не приходила я слышала одну и ту же фразу: "У вас нет опыта". А откуда ему было взяться тогда, я была выпускницей и очень хотела его получить, но к сожалению так никто и не дал.\n\n' +
                         'Моим главным навыком всегда бы вокал и я пошла работать в резеденцию "ЧАЙКА на пляже" в крыму в ялте, работала я певицей для того, чтобы заработать себе на жизнь, мне это нравилось, но я всегда чувствовала в себе потенциал гораздо больший, нежели быть просто певицей.Тогда я заинтересовалась SMM продвижением, которое как раз набирало свои обороты в популярности, я пошла в свою первую школу.\n\n' +
                         'Стоимость обучения была на тот момент 650 долларов и разбив сумму на две части я осилила и пошла обучаться, но не тут то было.' +
                         'С этой школой мне тоже не повезло, так как ценник был завышен, а знаний было процентов 20 из 100. Так и продолжался мой путь, я находила все больше и больше возможностей для того, чтобы обучиться и прочитала уйму литературы и простомотрела много семинаров, после нашла своего первого клиента и начала работать. Обучаясь на практике я начала осознавать некоторые вещи гораздо глубже, сталкивалась с различными ситуациями и трудностями, но никогда не останалвливалась и решала их без труда.\n\n' +
                         'Далее я стала обучаться уже у более квалифецированных международных специалистов оттачивая свои знания на практике. Время шло я получала все новые и новые навыки уже не только в продвижении, но и в инфо-запусках различных проектов и поняла, что готова создать свой.\n\n' +
                         'Я создала курс для тех, кто хочет освоить все инструменты продвижения в социальных сетях и успешно применять их на практике. Те, кто выбирают мою школу переходят на новый уровень мышления обретая навыки, которые помогают выйти на высокий уровень дохода.\n\n' +
                         'Но не всем хватает лишь знаний, для того, чтобы чувствовать себя экспертом, который уверен в себе и в своих силах, для меня важно развивать учеников со всех сторон. Поэтому последний модуль на курсе посвящен развитию уверенности в себе и поиску персонального таланта, обретению ораторского искусства и уверенности в завтрашнем дне!\n\n' +
                         'Сейчас мои мастер-классы посетило более 1500 человек и я с радость и гордостью выпустила первый потом учеников курса: ГОЛАЯ ПРАВДА SMM.\n\n' +
                         'Решение обучать студентов ко мне пришло после того, как я поняла, насколько инстаграм полон специалистами, которые не могу сделать ничего, а лишь обещают и гребут деньги за воду, которую льют в уши. Это не только мое мнение, так как после моих мастер-классов мне пишут отзывы и говорят о том, что столько полезной информации они не видели еще нигде и ни у кого. Я бесконечно счастлива всегда читать такие слова.\n\n' +
                         'Моя позиция такова: "Я НЕ БУДУ ДАВАТЬ ТЕБЕ ВОДУ, КОТОРУЮ ТЫ МОЖЕШЬ НАЛИТЬ СЕБЕ САМ". Только проверенная временем и опытом информация, которая поможет вам освоить все инструменты продвижения в ИНСТАГРАМ.\n\n' +
                         'Я верю в ТЕБЯ! Я ТОЧНО ЗНАЮ, ЧТО У ТЕБЯ ПОЛУЧИТЬСЯ, так как я рядом с тобой и смогу помочь тебе!\n\n' +
                         'ЖДУ тебя на 2-х дневном бесплатном мастре-классе и скорее переходи в нашу закрытую группу, где находятся остальные ребята!\n\n' +
                         '⏭ <a href="https://instagram.com/smm.league?igshid=1q2864gggcbhz"><b>ССЫЛКА НА ГРУППУ ЗДЕСЬ</b></a> ⏪\n\n' +
                         'С любовью и обнимашками, твоя Малинка❤️',
                         parse_mode='HTML')

    elif message.text == '🎁 Как получить бонус':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text='🎁 Скорее забирай свой подарок 🎁',
                                                        url="https://instagram.com/smm.league?igshid=1q2864gggcbhz")
        keyboard.add(url_button)
        bot.send_message(message.from_user.id,
                         'Перейти в нашу закрытую группу и написать в директ слово "БОНУС" И мы отправим его тебе!\n\n',
                         reply_markup=keyboard, parse_mode='HTML')

    elif message.text == '🔐 Закрытая группа мастер-класса':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text='⏭ Твоя персональная ссылка ⏪', url="https://instagram.com/smm.league?igshid=1q2864gggcbhz")
        keyboard.add(url_button)
        bot.send_message(message.from_user.id,
                         'Вся основная коммуникация будет проходить в нашей закрытой группе, сорее приссоеденяйся.\n\n',
                         reply_markup=keyboard, parse_mode='HTML')

    elif message.text == '📱 Связаться с нами':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text='Написать модератору', url="https://t.me/SL_help")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Привет! Нажми на кнопку чтобы получить помощь.', reply_markup=keyboard)


# /help
# @bot.message_handler(content_types=['Мастер-класс'])
# def help_command(message):
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     keyboard.add(
#         telebot.types.InlineKeyboardButton('VL', url='telegram.me/jeeeee', )
#     )
#     keyboard.add(
#         telebot.types.InlineKeyboardButton('IS', url='telegram.me/T_bI_III', )
#     )
#
#     bot.send_message(
#         message.chat.id,
#         'Если Вам нужна помощь или консультация, обратитесь к одному из специалистов:', reply_markup=keyboard
#     )

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)
#
# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.polling()
