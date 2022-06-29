from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

import keyboard
import createFront
import const


bot = Bot(token='5541380975:AAGI9U-DbTq7MC6mE5XPvRbKEaT76XKewNU')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, const.CONST_GREETINGS, reply_markup=keyboard.create_keyboard_front())


@dp.message_handler(commands=['/help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, const.CONST_HELP)


@dp.message_handler(lambda message: message.text == "В начало 😎")
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, const.CONST_GREETINGS, reply_markup=keyboard.create_keyboard_front())


# обработка кнопки О боте 🤖
@dp.message_handler(lambda message: message.text == "О боте 🤖")
async def without_puree(message: types.Message):
    msg = "Этот бот поможет вам выбрать шрифт и цвет для генерации текса.\n" \
          "✅ Запустите бота командой /start.\n" \
          "✅ Выберите шрифт.\n" \
          "✅ Выберите цвет.\n" \
          "✅ Отправьте боту фразу, которую хотите преобразить.\n" \
          "✅ Нажмите Сгенерировать текст 📝.\n"
    await bot.send_message(message.from_user.id, msg)


# обратка связи с автором
@dp.message_handler(lambda message: message.text == "Связаться с автором 👩🏽‍💻")
async def without_puree(message: types.Message):
    await bot.send_message(message.from_user.id, const.CONST_ANSWER)


# вывод доступных цветов
@dp.message_handler(lambda message: message.text == "Выбрать цвет 🎨")
async def without_puree(message: types.Message):
    # здесь inline-кнопки для выбора цвета
    photo = open('color.jpg', 'rb')
    # отправляем как документы, тогда фон остается прозрачным
    await bot.send_photo(message.from_user.id, photo, const.CONST_COLOR, reply_markup=keyboard.create_inline_board_color())
    # await bot.send_message(message.from_user.id, "выберите цвет", reply_markup=keyboard.create_inline_board_color())


# обработка нажатия кнопки выбора цвета
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_color'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    code2 = callback_query.data[-2]
    if code.isdigit():
        code = int(code)
        if code2.isdigit():
            code2 = int(code2)
            code = code2*10+code
    if code == 1:
        const.CONST_COLOR_NAME = "black"
        const.CUR_NUMBER_COLOR = "1"
    elif code == 2:
        const.CONST_COLOR_NAME = "white"
        const.CUR_NUMBER_COLOR = "2"
    elif code == 3:
        const.CONST_COLOR_NAME = "LightPink"
        const.CUR_NUMBER_COLOR = "3"
    elif code == 4:
        const.CONST_COLOR_NAME = "LightSkyBlue"
        const.CUR_NUMBER_COLOR = "4"
    elif code == 5:
        const.CONST_COLOR_NAME = "Khaki"
        const.CUR_NUMBER_COLOR = "5"
    elif code == 6:
        const.CONST_COLOR_NAME = "MediumAquamarine"
        const.CUR_NUMBER_COLOR = "6"
    elif code == 7:
        const.CONST_COLOR_NAME = "SlateBlue"
        const.CUR_NUMBER_COLOR = "7"
    elif code == 8:
        const.CONST_COLOR_NAME = "AntiqueWhite"
        const.CUR_NUMBER_COLOR = "8"
    elif code == 9:
        const.CONST_COLOR_NAME = "DodgerBlue"
        const.CUR_NUMBER_COLOR = "9"
    elif code == 10:
        const.CONST_COLOR_NAME = "Maroon"
        const.CUR_NUMBER_COLOR = "10"
    msg = "Выбран цвет № %s" % const.CUR_NUMBER_COLOR
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, msg)
    msg_all = "Введите фразу, к которой применить выбранные параметры:"
    await bot.send_message(callback_query.from_user.id, msg_all, reply_markup=keyboard.create_keyboard_color_generate())


# вывод доступных шрифтов
@dp.message_handler(lambda message: message.text == "Выбрать шрифт ✒️")
async def without_puree(message: types.Message):
    photo = open('front.jpg', 'rb')
    # отправляем как документы, тогда фон остается прозрачным
    await bot.send_photo(message.from_user.id, photo, const.CONST_FRONT, reply_markup=keyboard.create_inline_board_front())
    # await bot.send_message(message.from_user.id, "выберите один из них",)


# обработка нажатия кнопки выбора шрифта
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_front'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    code2 = callback_query.data[-2]
    if code.isdigit():
        code = int(code)
        if code2.isdigit():
            code2 = int(code2)
            code = code2*10+code
    if code == 1:
        const.CONST_FRONT_NAME = "PoiretOne-Regular.ttf"
        const.CUR_NUMBER_FRONT = "1"
    elif code == 2:
        const.CONST_FRONT_NAME = "ComforterBrush-Regular.ttf"
        const.CUR_NUMBER_FRONT = "2"
    elif code == 3:
        const.CONST_FRONT_NAME = "AmaticSC-Regular.ttf"
        const.CUR_NUMBER_FRONT = "3"
    elif code == 4:
        const.CONST_FRONT_NAME = "Pacifico-Regular.ttf"
        const.CUR_NUMBER_FRONT = "4"
    elif code == 5:
        const.CONST_FRONT_NAME = "Caveat-VariableFont_wght.ttf"
        const.CUR_NUMBER_FRONT = "5"
    elif code == 6:
        const.CONST_FRONT_NAME = "RubikGlitch-Regular.ttf"
        const.CUR_NUMBER_FRONT = "6"
    elif code == 7:
        const.CONST_FRONT_NAME = "MarckScript-Regular.ttf"
        const.CUR_NUMBER_FRONT = "7"
    elif code == 8:
        const.CONST_FRONT_NAME = "BadScript-Regular.ttf"
        const.CUR_NUMBER_FRONT = "8"
    elif code == 9:
        const.CONST_FRONT_NAME = "KleeOne-Regularr.ttf"
        const.CUR_NUMBER_FRONT = "9"
    elif code == 10:
        const.CONST_FRONT_NAME = "HachiMaruPop-Regular.ttf"
        const.CUR_NUMBER_FRONT = "10"
    elif code == 11:
        const.CONST_FRONT_NAME = "DotGothic16-Regular.ttf"
        const.CUR_NUMBER_FRONT = "11"
    # elif code == 12:
    #     const.CONST_FRONT_NAME = "Comforter-Regular.ttf"
    elif code == 12:
        const.CONST_FRONT_NAME = "Lobster-Regular.ttf"
        const.CUR_NUMBER_FRONT = "12"
    msg = "Выбран шрифт № %s" % const.CUR_NUMBER_FRONT
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, msg, reply_markup=keyboard.create_keyboard_color())


# генерация надписи
@dp.message_handler(lambda message: message.text == "Сгенерировать текст 📝")
async def without_puree(message: types.Message):
    if len(const.INPUT_TEXT) == 0:
        await bot.send_message(message.from_user.id, "Введите текст и нажмите еще раз кнопку")
        return
    createFront.transparent()
    photo = open(const.CUR_NAME, 'rb')
    await bot.send_document(message.chat.id, photo,  reply_markup=keyboard.create_keyboard_front())
    os.remove(const.CUR_NAME, dir_fd=None)
    const.INPUT_TEXT = ""


@dp.message_handler()
async def echo_message(message: types.Message):
    const.INPUT_TEXT = message.text
    msg = "Текст получен. Нажмите кнопку Сгенерировать текст 📝"
    await bot.send_message(message.from_user.id, msg, reply_markup=keyboard.create_keyboard_color_generate())


if __name__ == '__main__':
    executor.start_polling(dp)