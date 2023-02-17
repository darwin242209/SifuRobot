#import
import sqlite3
from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

#Bot data
OWNER_ID = 1744065403

# Initialize bot
bot = Bot(token='6274173401:AAGJsW474z1XNzUJXG4malvFkUo-pxigSMA')
dp = Dispatcher(bot)

# ------------------<Database Management>------------------
#Connect Database
conn = sqlite3.connect('BotDatabase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS chat_ids (chat_id INTEGER PRIMARY KEY)''')
c.execute('''CREATE TABLE IF NOT EXISTS user_ids (user_id INTEGER PRIMARY KEY)''')
conn.commit()
# ------------------<End>------------------

#-------------Topup Balance-----------------
#-------------------------------------------

#Contact Callback
@dp.callback_query_handler(lambda c: c.data == "contact")
async def contact_callback(callback_query: types.CallbackQuery):
    ws_button = InlineKeyboardButton(text="WhatsApp", url="https://api.whatsapp.com/send?phone=60104463636&text=Assalamualaikum%20Tuan")
    tele_button = InlineKeyboardButton(text="Telegram", url="t.me/SifuRobot769")
    tiktok_button = InlineKeyboardButton(text="Tik Tok", url="https://www.tiktok.com/@sifurobot769")
    back_button = InlineKeyboardButton(text="Back", callback_data="back")
    contact_Inline_Button = InlineKeyboardMarkup()
    contact_Inline_Button.add(ws_button, tele_button)
    contact_Inline_Button.add(tiktok_button)
    contact_Inline_Button.add(back_button)

    await bot.answer_callback_query(callback_query.id, text="Feel Free To Contact Us")
    await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Please Choose where you want to contact us",
                         reply_markup=contact_Inline_Button)

# Setup Inline Button
button1 = InlineKeyboardButton(text="Shop", callback_data="shop")
button2 = InlineKeyboardButton(text="Services", callback_data="servis")
contact_button = InlineKeyboardButton(text="Contact", callback_data="contact")
Sign_up_Button = InlineKeyboardButton(text="Sign Up", url="https://ask.je/daftarqm")
button5 = InlineKeyboardButton(text="Back", callback_data="back")

# Make Button In Bot
keyboard = InlineKeyboardMarkup()
keyboard.add(button1, button2)
keyboard.add(contact_button, Sign_up_Button)


#Callback For Back
@dp.callback_query_handler(lambda c: c.data == 'back')
async def cmd_start(callback_query: types.CallbackQuery):
  await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Hi, this is welcome message",
                         reply_markup=keyboard)


# Callback Shop Button
@dp.callback_query_handler(lambda c: c.data == "shop")
async def option1_callback(callback_query: types.CallbackQuery):
  button1_1 = InlineKeyboardButton(text="Barang 1", callback_data="barang1")
  button1_2 = InlineKeyboardButton(text="Barang 2", callback_data="barang2")
  back_button = InlineKeyboardButton("Back", callback_data="back")
  Shop_Item_Inline_Button = InlineKeyboardMarkup()
  Shop_Item_Inline_Button.add(button1_1, button1_2)
  Shop_Item_Inline_Button.add(back_button)

  await bot.answer_callback_query(callback_query.id, text="Welcome To Shop")
  await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Selamat Datang Ke Menu Kedai",
                         reply_markup=Shop_Item_Inline_Button)


#Callback Service Button
@dp.callback_query_handler(lambda c: c.data == "servis")
async def option2_callback(callback_query: types.CallbackQuery):
  button2_1 = InlineKeyboardButton(text="Whatsapp Marketing", callback_data="servis1")
  button2_2 = InlineKeyboardButton(text="Telegram Marketing", callback_data="servis2")
  button3_2 = InlineKeyboardButton(text="Facebook Marketing", callback_data="servis3")
  button4_2 = InlineKeyboardButton(text="SMS Marketing", callback_data="servis4")
  button5_2 = InlineKeyboardButton(text="Servis Follower", callback_data="servis5")
  button6_2 = InlineKeyboardButton(text="Tiktok Marketing", callback_data="servis6")
  button7_2 = InlineKeyboardButton(text="Instagram Marketing", callback_data="servis7")
  button8_2 = InlineKeyboardButton(text="Servis Landing Page QM", callback_data="servis8")
  button9_2 = InlineKeyboardButton(text="Servis Biolink & Landing Page", callback_data="servis9")
  back_button = InlineKeyboardButton("Back", callback_data="back")
  servis_keyboard = InlineKeyboardMarkup()
  servis_keyboard.add(button2_1, button2_2)
  servis_keyboard.add(button3_2, button4_2)
  servis_keyboard.add(button5_2, button6_2)
  servis_keyboard.add(button7_2, button8_2)
  servis_keyboard.add(button9_2)
  servis_keyboard.add(back_button)
  await bot.answer_callback_query(callback_query.id,
                                  text="Selamat datang ke menu servis")
  await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Please select Servis:",
                         reply_markup=servis_keyboard)


#Daftar CHANNEL /pair
@dp.message_handler(commands=['pair'])
async def pair_handler(message: types.Message):
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPERGROUP, types.ChatType.CHANNEL]:
        chat_id = message.chat.id
        c.execute('INSERT OR IGNORE INTO chat_ids (chat_id) VALUES (?)', (chat_id,))
        conn.commit()
        await message.reply("Chat paired successfully!")
    else:
        await message.reply("Maaf /pair hanya dapat digunakan di dalam 'channel' dan 'Group' sahaja.")

#Broadcast
@dp.message_handler(commands=['broad'])
async def broad_handler(message: types.Message):
    if message.from_user.id != OWNER_ID:
        await message.reply("You are not authorized to use this command.")
    else:
        await message.reply("Please enter your message to broadcast.")
        # Set up next handler to receive broadcast message
        dp.register_message_handler(broadcast_handler)

#Broadcast Handler
async def broadcast_handler(message: types.Message):
    # Get message to broadcast
    broadcast_text = message.text
    # Get all chat IDs and user IDs from database
    c.execute('SELECT chat_id FROM chat_ids')
    chat_ids = [row[0] for row in c.fetchall()]
    c.execute('SELECT user_id FROM user_ids')
    user_ids = [row[0] for row in c.fetchall()]
    # Send broadcast message to all chat IDs and user IDs
    for chat_id in chat_ids:
        await bot.send_message(chat_id, broadcast_text, parse_mode=ParseMode.HTML)
    for user_id in user_ids:
        await bot.send_message(user_id, broadcast_text, parse_mode=ParseMode.HTML)
    # Remove broadcast handler from dispatcher
    dp.unregister_message_handler(broadcast_handler)

# /start command handler
@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    c.execute('INSERT OR IGNORE INTO user_ids (user_id) VALUES (?)', (user_id,))
    conn.commit()
    await bot.send_message(chat_id=message.chat.id,
                         text="Hi,"+first_name+"!\n\nSelamat Datang ke I Am SifuRobot Official Bot\n\n𝘚𝘢𝘵𝘶-𝘴𝘢𝘵𝘶𝘯𝘺𝘢 Robot AI 𝘢𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘬 𝘺𝘢𝘯𝘨 100% 𝘮𝘦𝘮𝘦𝘯𝘶𝘩𝘪 𝘬𝘦𝘱𝘦𝘳𝘭𝘶𝘢𝘯 𝘢𝘯𝘥𝘢 - 'Automate Intelligent Your System'\n\n𝘉𝘪𝘢𝘳 𝘬𝘢𝘮𝘪 𝘣𝘢𝘯𝘵𝘶 𝘵𝘪𝘯𝘨𝘬𝘢𝘵𝘬𝘢𝘯 𝘫𝘶𝘢𝘭𝘢𝘯 𝘢𝘯𝘥𝘢 𝘥𝘦𝘯𝘨𝘢𝘯 '𝘛𝘰𝘰𝘭𝘴 𝘗𝘰𝘸𝘦𝘳 𝘡𝘦𝘳𝘰 𝘊𝘰𝘴𝘵 𝘔𝘢𝘳𝘬𝘦𝘵𝘪𝘯𝘨' 𝘋𝘢𝘳𝘪 pelbagai Platform & Provider Super Hebat.\n\n𝘋𝘦𝘯𝘨𝘢𝘯 𝘬𝘢𝘮𝘪 𝘢𝘯𝘥𝘢 𝘵𝘢𝘬 𝘱𝘦𝘳𝘭𝘶 𝘵𝘪𝘯𝘨𝘬𝘢𝘵𝘬𝘢𝘯 𝘣𝘢𝘫𝘦𝘵 𝘱𝘦𝘮𝘢𝘴𝘢𝘳𝘢𝘯 𝘢𝘯𝘥𝘢 𝘶𝘯𝘵𝘶𝘬 𝘥𝘢𝘱𝘢𝘵 10𝘟 𝘑𝘶𝘢𝘭𝘢𝘯 𝘥𝘦𝘯𝘨𝘢𝘯 𝘻𝘦𝘳𝘰 𝘤𝘰𝘴𝘵.\n\nSila klik button di bawah untuk Carian Pantas👇",
                         reply_markup=keyboard)


#run bot
if __name__ == '__main__':
  print("+ Bot Online Now")
  print("+ Visit https://t.me/SifuRobotBETAbot [BETA Version]")
  print("+ Visit https://t.me/SifuRobotShopBot [Official Version]")
  print(
    "~ Official version lebih stabil, BETA version bot untuk test run code ~")

  executor.start_polling(dp)
