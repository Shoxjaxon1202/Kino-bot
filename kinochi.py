import telebot
from telebot import types
BUT_TOKEN="8375049997:AAHd8vq0JwB6QB3uHdSDYfy6cjAc5TxIZV4"
bot=telebot.TeleBot(BUT_TOKEN)
@bot.message_handler(commands='start')
def start(message):
    markup=types.InlineKeyboardMarkup()
    button1=types.KeyboardButton("Sonic 4" )
    button2=types.KeyboardButton("Minecraft movie")
    button3=types.KeyboardButton("Pacific Rim 2")
    button4=types.KeyboardButton("Zombielend" )
    button5=types.KeyboardButton("Bluelock")
    button6=types.KeyboardButton("Pacific Rim" )
    button7=types.KeyboardButton("Sonic 3")
    button8=types.KeyboardButton("Avengers Doomsday")
    button9=types.KeyboardButton("Uch qahramon")
    button10=types.KeyboardButton("Pele")
    markup.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10)
    bot.send_message(message.chat.id,"Film tanlang",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def quer(call):
    if call.data == "sonic":
        a=open("351b673f.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "minecraft":
        a=open("4f31794e-477b-4c28-b0ab-dda35af496ac.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "rim2":
        a=open("pacific.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "zombie":
        a=open("zombie.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "bluelock":
        a=open("bluelock.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "rim":
        a=open("rim.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "sonic3":
        a=open("sonic.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "avengers":
        a=open("avengers.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "uch":
        a=open("uch.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "pele":
        a=open("pele.mp4","rb")
        bot.send_video(call.message.chat.id,a)
@bot.message_handler(func=lambda call:True)
def quer(message):
    b=message.text
    if int(b)==1:
        a=open("351b673f.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==2:
        a=open("4f31794e-477b-4c28-b0ab-dda35af496ac.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==3:
        a=open("pacific.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==4:
        a=open("zombie.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==5:
        a=open("bluelock.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==6:
        a=open("rim.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==7:
        a=open("sonic.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==8:
        a=open("avengers.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==9:
        a=open("uch.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==10:
        a=open("pele.mp4","rb")
        bot.send_video(message.chat.id,a)
print("Salom")
bot.infinity_polling()







# import telebot
# Token = "8375049997:AAHd8vq0JwB6QB3uHdSDYfy6cjAc5TxIZV4"
# bot = telebot.TeleBot(Token)
# @bot.message_handler(commands=['start'])
# def choose_day(message):
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     btn1 = telebot.types.KeyboardButton('Dushanba')
#     btn2 = telebot.types.KeyboardButton('Seshanba')
#     btn3 = telebot.types.KeyboardButton('Chorshanba')
#     btn4 = telebot.types.KeyboardButton('Payshanba')
#     btn5 = telebot.types.KeyboardButton('Juma')
#     btn6 = telebot.types.KeyboardButton('Shanba')

#     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, )
#     bot.send_message(message.chat.id, "Iltimos, kunni tanlang:", reply_markup=markup)


# print("Bot ishga tushdi")
# bot.infinity_polling()







import telebot #telegram bot kutuxonasi

token = "8452830462:AAHwDi9bQnAKerfWPwijayKMlrQUqSrRQ-o" #botga kirish uchun kalit
bot = telebot.TeleBot(token) #bot nomli o'zgaruvchini kalit bilan ochib olish bu endi aynan bizning bot

@bot.message_handler(commands=['start']) #bizni botga yozilgan xabarlarni ushlab oladi
#message_handler - bu xabarlarni ushlab olish. commands=['start'] aynan /start comandasi berilganda biror ish bajarish.
def send(message): #bu funksiya malum bir ishni bajarishga moslashgan
    bot.reply_to(message,"salom") #funksiyani vazifasi start yozilganda foydalanuvchiga qayta xabar jo'natish
#start yozilsa o'sha xabarga javob siafatida salom yuboriladi.

print("Dastur ishga tushdi") #dastur ishga tushganini bildirish uchun oddiy xabar terminalda
bot.infinity_polling() #botga qayta qayta yozishga yordam beradigan buyruq














































# import telebot
# from telebot import types

# TOKEN = "8250156289:AAG4JjRS50gcucsWcLpRW-iumfVKxz4m5to"
# bot = telebot.TeleBot(TOKEN)

# CHANNELS = [
#     "https://t.me/shoxjaxon_kinochi",
#     "@shoxjaxon_python_bot"
# ]

# def check_user(user_id):
#     for ch in CHANNELS:
#         try:
#             status = bot.get_chat_member(ch, user_id).status
#             if status in ['left', 'kicked']:
#                 return False
#         except:
#             return False
#     return True

# from pymongo import MongoClient

# MONGO_URL = "mongodb+srv://shoxjaxonabdusalimov1202_db_user:3OflKlEv3UuES6qx@cluster0.ygcbmv9.mongodb.net/"
# client = MongoClient(MONGO_URL)

# db = client["kinochi_bot"]
# collection = db["videos"]

# @bot.channel_post_handler(content_types=["video"])
# def handle_channel_post(message):
#     if message.chat.username == "":
#         collection.insert_one({
#             "file_id": message.video.file_id,
#             "caption": message.caption
#         })

# def IsSubscribe(chat_id):
#     markup = types.InlineKeyboardMarkup()

#     for ch in CHANNELS:
#         markup.add(types.InlineKeyboardButton(text=ch, url=f"https://t.me/{ch[1:]}"))

#     markup.add(types.InlineKeyboardButton("tekshirish", callback_data="check"))

#     bot.send_message(chat_id, "botdan foydalanish uchun kanallarga obuna boling", reply_markup=markup)

# @bot.message_handler(commands=['start'])
# def start(message):
#     user_id = message.from_user.id
#     if check_user(user_id):
#         bot.send_message(message.chat.id, "botdan foydalanishingiz mumkin!")
#     else:
#         IsSubscribe(message.chat.id)

# @bot.callback_query_handler(func=lambda call: call.data == "check")
# def check_callback(call):
#     user_id = call.from_user.id
#     if check_user(user_id):
#         bot.send_message(call.message.chat.id, "botdan foydalanishingiz mumkin!")
#     else:
#         bot.send_message(call.message.chat.id, "barcha kanallarga obuna bo'lmagansiz!")

# @bot.message_handler(func=lambda message: True)
# def all_messages(message):
#     user_id = message.from_user.id
#     if not check_user(user_id):
#         IsSubscribe(message.chat.id)
#         return

#     if message.text.isdigit():
#         for video in collection.find():
#             if f"Kod: {message.text}" in video["caption"]:
#                 bot.send_video(
#                     message.chat.id, 
#                     video["file_id"], 
#                     caption=video["caption"]
#                 )
#     else:
#         bot.send_message(message.chat.id, "Error 404")

# bot.polling()




# sonlar = (3,5,8,9,10)
# ortacha = 0
# for i in sonlar:
#     ortacha += i

# print(ortacha / 5)















# for i in range(1,10,2): 
#     for j in range(1,10,2): 
#         print(i,j)

























