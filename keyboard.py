from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def create_keyboard_front():
    button = KeyboardButton('Выбрать шрифт ✒️')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('О боте 🤖', callback_data='about'))
    markup.add(KeyboardButton('Связаться с автором 👩🏽‍💻', callback_data='author'))
    markup.add(KeyboardButton('Назад 😎', callback_data='return'))
    return markup


def create_keyboard_color():
    button = KeyboardButton('Выбрать цвет 🎨')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('О боте 🤖', callback_data='about'))
    markup.add(KeyboardButton('Связаться с автором 👩🏽‍💻', callback_data='author'))
    markup.add(KeyboardButton('Назад 😎', callback_data='return'))
    return markup


def create_keyboard_color_generate():
    button = KeyboardButton('Сгенерировать текст 📝')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button)
    markup.add(KeyboardButton('О боте 🤖', callback_data='about'))
    markup.add(KeyboardButton('Связаться с автором 👩🏽‍💻', callback_data='author'))
    markup.add(KeyboardButton('Назад 😎', callback_data='return'))
    return markup


# создаем клавиатуру дял цветовой плалитры
def create_inline_board_color():
    inline_btn_1 = InlineKeyboardButton('1️⃣', callback_data='btn_color1')
    inline_btn_2 = InlineKeyboardButton('2️⃣', callback_data='btn_color2')
    inline_btn_3 = InlineKeyboardButton('3️⃣', callback_data='btn_color3')
    inline_btn_4 = InlineKeyboardButton('4️⃣', callback_data='btn_color4')
    inline_btn_5 = InlineKeyboardButton('5️⃣', callback_data='btn_color5')
    inline_kb_full = InlineKeyboardMarkup(row_width=5).add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4,
                                                           inline_btn_5)

    inline_btn_6 = InlineKeyboardButton('6️⃣', callback_data='btn_color6')
    inline_btn_7 = InlineKeyboardButton('7️⃣', callback_data='btn_color7')
    inline_btn_8 = InlineKeyboardButton('8️⃣', callback_data='btn_color8')
    inline_btn_9 = InlineKeyboardButton('9️⃣', callback_data='btn_color9')
    inline_btn_10 = InlineKeyboardButton('🔟', callback_data='btn_color10')
    inline_kb_full.add(inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10)

    return inline_kb_full


def create_inline_board_front():
    inline_btn_1 = InlineKeyboardButton('1️⃣', callback_data='btn_front1')
    inline_btn_2 = InlineKeyboardButton('2️⃣', callback_data='btn_front2')
    inline_btn_3 = InlineKeyboardButton('3️⃣', callback_data='btn_front3')
    inline_kb_full = InlineKeyboardMarkup(row_width=3).add(inline_btn_1, inline_btn_2, inline_btn_3)

    inline_btn_4 = InlineKeyboardButton('4️⃣', callback_data='btn_front4')
    inline_btn_5 = InlineKeyboardButton('5️⃣', callback_data='btn_front5')
    inline_btn_6 = InlineKeyboardButton('6️⃣', callback_data='btn_front6')
    inline_kb_full.add(inline_btn_4, inline_btn_5, inline_btn_6)

    inline_btn_7 = InlineKeyboardButton('7️⃣', callback_data='btn_front7')
    inline_btn_8 = InlineKeyboardButton('8️⃣', callback_data='btn_front8')
    inline_btn_9 = InlineKeyboardButton('9️⃣', callback_data='btn_front9')
    inline_kb_full.add(inline_btn_7, inline_btn_8, inline_btn_9)

    inline_btn_10 = InlineKeyboardButton('🔟', callback_data='btn_front10')
    inline_btn_11 = InlineKeyboardButton('1️⃣1️⃣', callback_data='btn_front11')
    inline_btn_12 = InlineKeyboardButton('1️⃣2️⃣', callback_data='btn_front12')
    # inline_btn_13 = InlineKeyboardButton('1️⃣3️⃣', callback_data='btn_front13')
    inline_kb_full.add(inline_btn_10, inline_btn_11, inline_btn_12)

    return inline_kb_full
