from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CHANNEL_ID = []
OWNER_ID = 1744065403
USER_LIST = []

# Initialize bot and dispatcher
bot = Bot(token='6192057464:AAFbZ4_5JuIICXG40Fp4sDGLlNq8qWvErpw')
dp = Dispatcher(bot)

# First inline button
button1 = InlineKeyboardButton(text="Shop", callback_data="option1")
button2 = InlineKeyboardButton(text="Services", callback_data="option2")
button3 = InlineKeyboardButton(text="Contact Us", callback_data="option2")

# Initial inline menu
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

# Callback function for first inline button
@dp.callback_query_handler(lambda c: c.data == "option1")
async def option1_callback(callback_query: types.CallbackQuery):
    button1_1 = InlineKeyboardButton(text="Sub-Option 1", callback_data="suboption1_1")
    button1_2 = InlineKeyboardButton(text="Sub-Option 2", callback_data="suboption1_2")
    sub_keyboard_inline = InlineKeyboardMarkup().add(button1_1, button1_2)

    await bot.answer_callback_query(callback_query.id, text="Option 1 selected")
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="Please select a sub-option:",
        reply_markup=sub_keyboard_inline
    )

# Callback function for second inline button
@dp.callback_query_handler(lambda c: c.data == "option2")
async def option2_callback(callback_query: types.CallbackQuery):
    button2_1 = InlineKeyboardButton(text="Sub-Option 1", callback_data="suboption2_1")
    button2_2 = InlineKeyboardButton(text="Sub-Option 2", callback_data="suboption2_2")
    sub_keyboard_inline = InlineKeyboardMarkup().add(button2_1, button2_2)

    await bot.answer_callback_query(callback_query.id, text="Option 2 selected")
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="Please select a sub-option:",
        reply_markup=sub_keyboard_inline
    )

@dp.message_handler(commands='broad')
async def cmd_broadcast(message: types.Message):
    if message.from_user.id == OWNER_ID:
        reply_text = message.reply_to_message.text
        # Send the reply text to all users in the USER_LIST
        for user_id in USER_LIST:
            await bot.send_message(chat_id=user_id, text=reply_text)
        await bot.send_message(chat_id=message.chat.id, text="Broadcast complete! Sent to all users.")
    else:
        await bot.send_message(chat_id=message.chat.id, text="Error: Sorry, this command can only be used by the owner."
    )

# /start command handler
@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    if message.chat.id not in USER_LIST:
        USER_LIST.append(message.chat.id)
    await bot.send_message(
        chat_id=message.chat.id,
        text="Please select an option:",
        reply_markup=keyboard_inline
    )


if __name__ == '__main__':
    print("+ Bot Online Now")
    executor.start_polling(dp)
