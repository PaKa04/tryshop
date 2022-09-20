import telebot
from database import Market
from telebot import types


db = Market()
bot = telebot.TeleBot("")
To_chat_id = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Добро пожаловать,{message.from_user.first_name},'
                                      f' в этом магазине вы можете преобрести товары по лучшим ценам')
    db.registration(message.chat.id, message.from_user.first_name, message.from_user.last_name, f'@{message.from_user.username}')
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Iphone 11', callback_data='iphone')
    btn2 = types.InlineKeyboardButton(text='Macbook', callback_data='mac')
    btn3 = types.InlineKeyboardButton(text='apple-watch', callback_data='apple_watch')
    btn4 = types.InlineKeyboardButton(text='Samsung', callback_data='samsung')
    btn5 = types.InlineKeyboardButton(text='Notebook ASUS', callback_data='asus')
    btn6 = types.InlineKeyboardButton(text='Samsung-watch', callback_data='samsung-watch')
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id,
                     'Нажмите на кнопку, в зависимости от интересующего вас товара'.format(message.from_user),
                     reply_markup=keyboard)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Посмотреть корзину')
    button2 = types.KeyboardButton('МЕНЮ')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Для заказа используйте встроенные в клавиатуру кнопки", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):

    if call.data == 'iphone':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Добавить в корзину ', callback_data='-iphone')
        markup.add(btn)
        bot.send_photo(call.message.chat.id, open('C:\\Users\\123\\Pictures\\iphone_11.jpg', 'rb'), caption='Смартфон корпорации Apple, использующий процессор Apple A13 Bionic который содержит 8,5 млрд транзисторов и операционную систему iOS 13, представленный 10 сентября 2019 года вместе с iPhone 11 Pro и iPhone 11 Pro Max. Является преемником iPhone XR.\nЦена: 40,00 BYN\nДля добавления в корзину нажмите кнопку ниже',
                         reply_markup=markup)
    elif call.data == 'mac':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Добавить в корзину ', callback_data='-mac')
        markup.add(btn)
        bot.send_photo(call.message.chat.id, open('C:\\Users\\123\\Pictures\\mac.jpg', 'rb'),
                   caption='Линейка ноутбуков серии MacBook с 13,6-дюймовым экраном, выпускаемых компанией Apple с 2008 года, с 2016 по 2022 выпускалась 13,3" версия, а с 2010 по 2016 выпускался 11,6" вариант\nЦена: 6879,99 BYN\nДля добавления в корзину нажмите кнопку ниже',
                         reply_markup=markup)

    elif call.data == 'apple_watch':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Добавить в корзину ', callback_data='-aw')
        markup.add(btn)
        bot.send_photo(call.message.chat.id, open('C:\\Users\\123\\Pictures\\aw.jpg', 'rb'), caption='Линейка умных часов, созданных корпорацией Apple и представленные 9 сентября 2014 года. Для их полноценной работы требуется смартфон iPhone 5 или новее с IOS 8 или новее. Apple Watch были выпущены в апреле 2015 года и быстро стали самым продаваемым носимым устройством: во втором квартале 2015 финансового года было продано 4,2 миллиона устройств, и, по оценкам, более 100 миллионов человек использовали Apple Watch по состоянию на декабрь 2020 года.\nЦена: 3,00 BYN\nДля добавления в корзину нажмите кнопку ниже',
                         reply_markup=markup)

    elif call.data == 'samsung':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Добавить в корзину ', callback_data='-samsung')
        markup.add(btn)
        bot.send_photo(call.message.chat.id, open('C:\\Users\\123\\Pictures\\samsung.jpg', 'rb'), caption='Линейка смартфонов на базе Android, разработанных, продаваемых и производимых компанией Samsung Electronics в рамках своей серии Galaxy S. Эта серия является преемником серий Galaxy S21 и Galaxy Note 20. Линейка была представлена на мероприятии Samsung Galaxy Unpacked 9 февраля 2022 года. Продажи начались 1 марта. Продажи в Российской Федерации были отменены.\nЦена: 0,8 BYN\nДля добавления в корзину нажмите кнопку ниже',
                         reply_markup=markup)


    elif call.data == 'asus':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Добавить в корзину ', callback_data='-asus')
        markup.add(btn)
        bot.send_photo(call.message.chat.id, open('C:\\Users\\123\\Pictures\\asus.jpg', 'rb'), caption='Игровой ноутбук ASUS ROG Strix G15 G513RC-HN13315.6" 1920 x 1080 IPS, 144 Гц, несенсорный, AMD Ryzen 7 6800H 3200 МГц, 16 ГБ DDR5, SSD 512 ГБ, видеокарта NVIDIA GeForce RTX 3050 4 ГБ, без ОС, цвет крышки черный\nЦена: 5600,00 BYN\nДля добавления в корзину нажмите кнопку ниже',
                         reply_markup=markup)

    elif call.data == 'samsung-watch':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Добавить в корзину ', callback_data='-sw')
        markup.add(btn)
        bot.send_photo(call.message.chat.id, open('C:\\Users\\123\\Pictures\\sw.jpg', 'rb'), caption='Умные часы, разработанные компанией Samsung Electronics. Об этом было объявлено 9 августа 2018 года. Поступление Galaxy Watch в продажу в Соединенных Штатах было запланировано на 24 августа 2018 года, в некоторых операторах связи и торговых точках в Южной Корее - на 31 августа 2018 года, а на дополнительных избранных рынках - на 14 сентября 2018 года.\nЦена: 600,00 BYN\nДля добавления в корзину нажмите кнопку ниже',
                         reply_markup=markup)

    elif call.data == 'clear':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        db.clear_bucket(call.message.chat.id)

    elif call.data == 'buy':
        bot.send_message(To_chat_id, f'Новый заказ\n покупатель: {db.zakaz(call.message.chat.id)}\n '
                                          f'Заказ:{db.showbucket(call.message.chat.id)}')
        bot.send_message(call.message.chat.id, "Заказ сделан")
    for key, value in {'-sw':'samsung-watch', '-asus':"asus", '-samsung':'samsung', '-aw':'apple-watch', '-iphone':'iphone', '-mac':'macbook'}.items():
        if call.data == key:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            db.inbucket(call.message.chat.id, value)


@bot.message_handler(content_types=['text'])
def answertext(message):
    if message.text == 'Посмотреть корзину':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear')
        btn2 = types.InlineKeyboardButton(text='Заказать', callback_data='buy')
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, db.showbucket(message.chat.id), reply_markup=keyboard)
    elif message.text == 'МЕНЮ':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Iphone 11', callback_data='iphone')
        btn2 = types.InlineKeyboardButton(text='Macbook', callback_data='mac')
        btn3 = types.InlineKeyboardButton(text='apple-watch', callback_data='apple_watch')
        btn4 = types.InlineKeyboardButton(text='Samsung', callback_data='samsung')
        btn5 = types.InlineKeyboardButton(text='Notebook ASUS', callback_data='asus')
        btn6 = types.InlineKeyboardButton(text='Samsung-watch', callback_data='samsung-watch')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id,
                         'Нажмите на кнопку, в зависимости от интересующего вас товара'.format(message.from_user),
                         reply_markup=keyboard)


bot.infinity_polling(none_stop=True, interval=0)
