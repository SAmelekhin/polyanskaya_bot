import os

from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, ConversationHandler

MAIN_DIR = os.getcwd()
FILES_DIR = os.path.join(MAIN_DIR, 'files')
FIRST_LESSON_DIR = os.path.join(FILES_DIR, 'first_lesson')

if __name__ == '__main__':
    updater = Updater(token='5938512415:AAGWUclAPiZUKJ8dA-sQI1hfR9PVr8F1J2Q')

    remarks_sequence = {
        'VIDEO_INTRO': 0,
        'PROLOGUE_AUDIO': 1,
        'PROLOGUE_IMAGE': 2,
        'PROLOGUE_TEXT': 3,
        '1_REMARK': 4,
        '1_1_REMARK': 5,  # TODO NEW
        '1_2_REMARK': 6,  # TODO NEW
        '2_REMARK': 7,
        '3_REMARK': 8,
        '4_REMARK': 9,
        '5_REMARK': 10,
        '6_REMARK': 11,
        '7_REMARK': 12,
        '8_REMARK': 13,
        '9_REMARK': 14,
        '10_REMARK': 15,
        '11_REMARK': 16,
        '12_REMARK': 17,
        '12_1_REMARK': 18,  # TODO NEW
        '13_REMARK': 19,
        '14_REMARK': 20,
        '15_REMARK': 21,
        '16_REMARK': 22,
        '17_REMARK': 23,
        '18_REMARK': 24,
        '19_REMARK': 25,
        '20_REMARK': 26,
        '21_REMARK': 27,
        '22_REMARK': 28,
        '23_REMARK': 29,
    }


    def video_intro(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Здорово! Что дальше?  \U0001F3A7 '], ])
        context.bot.send_video_note(
            chat_id=chat.id,
            video_note=open(os.path.join(FIRST_LESSON_DIR, 'видео_введение_new.mp4'), 'rb'),
            reply_markup=buttons,
        )
        return remarks_sequence.get('PROLOGUE_AUDIO')


    def prologue_audio(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Отправиться в Лесные дали Мнемоземья навстречу испытаниям'], ])
        context.bot.send_voice(
            chat_id=chat.id,
            voice=open(os.path.join(FIRST_LESSON_DIR, 'аудио_введение_new.mp3'), 'rb'),
            reply_markup=buttons,
        )
        return remarks_sequence.get('PROLOGUE_IMAGE')


    def prologue_image(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Вот ты и на месте!'], ])
        context.bot.send_photo(
            chat_id=chat.id,
            photo=open(os.path.join(FIRST_LESSON_DIR, 'лесные дали мнемоземья карточка.png'), 'rb'),
            reply_markup=buttons,
        )
        return remarks_sequence.get('PROLOGUE_TEXT')


    def welcome_text_1(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Здравствуйте'], ['Приветики!']])
        context.bot.send_photo(
            chat_id=chat.id,
            reply_markup=buttons,
            photo=open(os.path.join(FIRST_LESSON_DIR, 'Селестина Мемория карточка.png'), 'rb'),
            caption='Добро пожаловать в Лесные дали Мнемоземья, храбрый путник!',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('1_REMARK')


    def welcome_text_2(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Разве ты не эльф? У тебя такие уши...']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nЯ —  Селестина Мемория, старшая фея Мнемоземья. ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('1_1_REMARK')


    def welcome_text_3(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['\U0001F60D'], ['\U0001F44D']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nУ меня в роду были эльфы, но все-таки я фея, не сомневайся. ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('1_2_REMARK')


    def welcome_text_4(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Я спасу Мнемоземье!'], ['Я задам трепку злодею!']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nЯ слышала, что ты пришел, чтобы спасти наше прекрасное Мнемоземье от несчастья, '
                 'которое постигло нас из-за козней злодея Мракмора Обливиона.',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('2_REMARK')


    def dialog_line_1(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Не сомневаюсь'], ['Я постараюсь']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nЧтобы вернуть украденные знания, '
                 'тебе нужно научиться мнемотехникам. '
                 'Ты справишься?',
            parse_mode=ParseMode.HTML,

        )
        return remarks_sequence.get('3_REMARK')


    def dialog_line_2(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Это что-то волшебное?'], ['Я уже знаю, что это']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nЯ помогу тебе на этом нелегком пути, ведь память — это важнейшее сокровище. '
                 'А теперь тебе нужно узнать о том, что такое мнемотехники. ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('4_REMARK')


    def dialog_line_3(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Звучит удивительно!'], ['Как же я смогу им научиться?']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nЭто почти магия, ведь мнемотехники — это специальные трюки и секреты, '
                 'которые помогают нам запоминать информацию лучше и хранить в памяти дольше.',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('5_REMARK')


    def dialog_line_4(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['\U0001F9D9'], ['\U0001F44D']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b> '
                 '\nПосмотри вокруг!'
                 ' Эти старые деревья, которые растут в Лесных далях — наши учителя.'
                 ' Они хранят множество знаний и тайн Мнемоземья.',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('6_REMARK')


    def dialog_line_5(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Начнём обучение'], ['Как это работает?']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nДавай начнем с простой мнемотехники — "Прием первой буквы"',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('7_REMARK')


    def dialog_line_6(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Конечно! '], ['Нет']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nТы знаешь, как легко выучить все цвета радуги?',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('8_REMARK')


    def dialog_line_7(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['О, это я знаю!'], ['Не знаю такую']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nКак раз в этом нам помогает «Прием первой буквы». '
                 'С детства многим знакома фраза: «Каждый Охотник Желает Знать, Где Сидит Фазан»',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('9_REMARK')


    def dialog_line_8(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Ничего себе!'], ['Понятно']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 f'\nЗдесь каждое слово начинается с буквы, с которой начинается и название цвета:'
                 f' красный, оранжевый, желтый, зеленый, голубой, синий и фиолетовый.'
                 f' Так можно легко запомнить последовательность цветов радуги. ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('10_REMARK')


    def dialog_line_9(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Это легко!'], ['Хорошо, что дальше?']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nЭто одна из мнемотехник, которую тебе нужно освоить, чтобы победить Мракмора Обливиона! ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('11_REMARK')


    def dialog_line_10(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Сейчас приступлю к заданию']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nА теперь потренируйся использовать «Прием первой буквы». '
                 'Когда ты справишься, то получишь волшебный артефакт. '
                 'Без него ты не сможешь продолжить свое героическое путешествие. ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('12_REMARK')


    def dialog_line_10_1(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Уже готово!']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<a href="https://coreapp.ai/app/player/lesson/6541023b7634ea7f1551491e/">Пройти испытание</a>'
                 f'\n\nНажми "Уже готово", когда пройдешь испытание',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('12_1_REMARK')


    def dialog_line_11(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Ура!'], ['Спасибо']])
        context.bot.send_photo(
            chat_id=chat.id,
            reply_markup=buttons,
            photo=open(os.path.join(FIRST_LESSON_DIR, 'артефакт карта сокровищ карточка.png'), 'rb'),
            caption=f'<b>Селестина Мемория \U0001F9DA :</b>'
                    '\nПоздравляю, ты достойно справился с первым испытанием! '
                    '\nЭта карта сокровищ \U0001F5FA — твой первый артефакт. '
                    'Очень скоро она пригодится тебе.',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('13_REMARK')


    def dialog_line_12(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Ой, кто это?'], ['Какой милый']])
        context.bot.send_photo(
            chat_id=chat.id,
            reply_markup=buttons,
            photo=open(os.path.join(FIRST_LESSON_DIR, 'пушистик карточка.png'), 'rb'),
        )
        return remarks_sequence.get('14_REMARK')


    def dialog_line_13(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Какая у тебя загадка? \U0001F914 ']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nА это Пушистик. Он многое помнит и обожает загадки.'
                 ' Пушистик будет твоим спутником и помощником в Мнемоземье.'
                 ' Пушистик, загадай нам загадку! ',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('15_REMARK')


    def dialog_line_14(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Да'], ['Нет']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Пушистик \U0001F43E :</b>'
                 '\nРад познакомиться!'
                 '\nПравда ли, что запоминание бывает видом спорта?',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('16_REMARK')


    def dialog_line_15(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['\U0001F632'], ['\U0001F60A']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Пушистик \U0001F43E :</b>'
                 '\nЭто правда! Мнемоспорт относится к соревнованиям, в которых участники пытаются запомнить, '
                 'а потом вспомнить разные виды информации, используя мнемотехники.'
                 ' Существуют даже чемпионаты по мнемоспорту — национальные (например, в России) и международные.',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('17_REMARK')


    def dialog_line_16(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Да! \U0001F4AA '], ])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Пушистик \U0001F43E :</b>'
                 '\nЯ уверен, что ты умный и старательный ученик. Вместе мы сможем вернуть знания и спасти Мнемоземье!',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('18_REMARK')


    def dialog_line_17(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Вперёд!'], ['Спасибо, фея!']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text=f'<b>Селестина Мемория \U0001F9DA :</b>'
                 '\nЧто ж, вам пора в путь. '
                 'Тебе предстоит отправиться на затерянный остров, известный своими сокровищами.'
                 ' Не забывай меня! Удачи!',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('19_REMARK')


    def dialog_line_18(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Супер!'], ['Ок']])
        context.bot.send_video_note(
            chat_id=chat.id,
            reply_markup=buttons,
            video_note=open(os.path.join(FIRST_LESSON_DIR, 'прогресс_с_ фанфарами_new.mp4'), 'rb'),
        )
        return remarks_sequence.get('20_REMARK')


    def dialog_line_19(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Что дальше?']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text='\U0001F389 \U0001F973 Поздравляю! Завершена 1 глава истории. Осталось 6 глав.',
        )
        return remarks_sequence.get('21_REMARK')


    def dialog_line_20(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Продолжить \U000027A1 ']])
        context.bot.send_photo(
            chat_id=chat.id,
            reply_markup=buttons,
            photo=open(os.path.join(FIRST_LESSON_DIR, 'mnemotechnics_first_letter.png'), 'rb'),
        )
        return remarks_sequence.get('22_REMARK')


    def dialog_line_21(update, context):
        chat = update.effective_chat
        buttons = ReplyKeyboardMarkup([['Хочу продолжить путешествие']])
        context.bot.send_message(
            chat_id=chat.id,
            reply_markup=buttons,
            text='Тебе понравилась первая глава истории о Мнемоземье?'
                 '\n<a href="https://docs.google.com/forms/d/1R2IShNSLLxXGRT4ari9kkO1Xh8phNFugujoV_UD4DXs/edit">Поделись</a>'
                 ' своими впечатлениями — так ты поможешь сделать обучающую игру лучше и интереснее.'
                 '\nА ещё, заполнив форму, ты получишь скидку 30% на весь курс \U0001F609',
            parse_mode=ParseMode.HTML,
        )
        return remarks_sequence.get('23_REMARK')


    def cancel(update, context):
        chat = update.effective_chat
        update.message.reply_text(
            text='Чтобы продолжить, оплати курс "Путешествие в Мнемоземье: секреты забытых знаний".',
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END


    converstation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', video_intro)],

        states={
            remarks_sequence.get('PROLOGUE_AUDIO'): [MessageHandler(Filters.all, prologue_audio)],
            remarks_sequence.get('PROLOGUE_IMAGE'): [MessageHandler(Filters.all, prologue_image)],
            remarks_sequence.get('PROLOGUE_TEXT'): [MessageHandler(Filters.all, welcome_text_1)],
            remarks_sequence.get('1_REMARK'): [MessageHandler(Filters.all, welcome_text_2)],
            remarks_sequence.get('1_1_REMARK'): [MessageHandler(Filters.all, welcome_text_3)],
            remarks_sequence.get('1_2_REMARK'): [MessageHandler(Filters.all, welcome_text_4)],
            remarks_sequence.get('2_REMARK'): [MessageHandler(Filters.all, dialog_line_1)],
            remarks_sequence.get('3_REMARK'): [MessageHandler(Filters.all, dialog_line_2)],
            remarks_sequence.get('4_REMARK'): [MessageHandler(Filters.all, dialog_line_3)],
            remarks_sequence.get('5_REMARK'): [MessageHandler(Filters.all, dialog_line_4)],
            remarks_sequence.get('6_REMARK'): [MessageHandler(Filters.all, dialog_line_5)],
            remarks_sequence.get('7_REMARK'): [MessageHandler(Filters.all, dialog_line_6)],
            remarks_sequence.get('8_REMARK'): [MessageHandler(Filters.all, dialog_line_7)],
            remarks_sequence.get('9_REMARK'): [MessageHandler(Filters.all, dialog_line_8)],
            remarks_sequence.get('10_REMARK'): [MessageHandler(Filters.all, dialog_line_9)],
            remarks_sequence.get('11_REMARK'): [MessageHandler(Filters.all, dialog_line_10)],
            remarks_sequence.get('12_REMARK'): [MessageHandler(Filters.all, dialog_line_10_1)],
            remarks_sequence.get('12_1_REMARK'): [MessageHandler(Filters.all, dialog_line_11)],
            remarks_sequence.get('13_REMARK'): [MessageHandler(Filters.all, dialog_line_12)],
            remarks_sequence.get('14_REMARK'): [MessageHandler(Filters.all, dialog_line_13)],
            remarks_sequence.get('15_REMARK'): [MessageHandler(Filters.all, dialog_line_14)],
            remarks_sequence.get('16_REMARK'): [MessageHandler(Filters.all, dialog_line_15)],
            remarks_sequence.get('17_REMARK'): [MessageHandler(Filters.all, dialog_line_16)],
            remarks_sequence.get('18_REMARK'): [MessageHandler(Filters.all, dialog_line_17)],
            remarks_sequence.get('19_REMARK'): [MessageHandler(Filters.all, dialog_line_18)],
            remarks_sequence.get('20_REMARK'): [MessageHandler(Filters.all, dialog_line_19)],
            remarks_sequence.get('21_REMARK'): [MessageHandler(Filters.all, dialog_line_20)],
            remarks_sequence.get('22_REMARK'): [MessageHandler(Filters.all, dialog_line_21)],
            remarks_sequence.get('23_REMARK'): [MessageHandler(Filters.all, cancel)],
        },
        fallbacks=[MessageHandler(Filters.regex(r'^Хочу продолжить путешествие$'), cancel)],
        allow_reentry=True,
    )

    updater.dispatcher.add_handler(converstation_handler)
    updater.start_polling()
    updater.idle()
