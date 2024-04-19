import paho.mqtt.client as q
import telebot as t
from telebot import types as ty
import time
import art
on_off = True
art.tprint('BOT IS ONLINE')
print('SEvaORG©')
m5 = q.Client(q.CallbackAPIVersion.VERSION1)
m5.connect("broker.hivemq.com", 1883, 300)
m5.subscribe('testopic/2',0)
bot = t.TeleBot('7195327169:AAG2UXyEqFFu0DT9HnxpsZZAwbP9khiwAsM')
@bot.message_handler(commands=['comms', 'start'])
def on_message(message):
    markup = ty.InlineKeyboardMarkup(row_width=1)
    i1 = ty.InlineKeyboardButton('прямо', callback_data='stra')
    i2 = ty.InlineKeyboardButton('назад', callback_data='beh')
    i3 = ty.InlineKeyboardButton('влево', callback_data='lef')
    i4 = ty.InlineKeyboardButton('вправо', callback_data='rig')
    i5 = ty.InlineKeyboardButton('громкий гудок', callback_data='hor')
    i6 = ty.InlineKeyboardButton('отключиться', callback_data='reb')
    i = ty.InlineKeyboardButton('прямо(по прямой)', callback_data='str')
    markup.add(i,i1,i2,i3,i4,i5,i6)
    bot.send_message(message.chat.id, 'перед тем как бездумно тыкать на кнопочки, зайдите сюда-> https://www.hivemq.com/demos/websocket-client/, а после создайте заголовок "testopic/2".Ну а чтобы получить код на РОбота просто пропишите ниже комманду "/code", а если вы все сделали, то зацените эти комманды: "/chBg", "/assis_msgs_onoff"', reply_markup=markup)
@bot.message_handler(commands=['chBg'])
def chSm(message):
  chbg= ty.InlineKeyboardMarkup(row_width=1)
  q1 =  ty.InlineKeyboardButton('красный', callback_data='re')
  q2 =  ty.InlineKeyboardButton('оранжевый', callback_data='or')
  q3 =  ty.InlineKeyboardButton('желтый', callback_data='ye')
  q4 =  ty.InlineKeyboardButton('зеленый', callback_data='gr')
  q5 =  ty.InlineKeyboardButton('голубой', callback_data='cy')
  q6 =  ty.InlineKeyboardButton('синий', callback_data='bl')
  q7 =  ty.InlineKeyboardButton('фиолетовый', callback_data='pu')
  chbg.add(q1,q2,q3,q4,q5,q6,q7)
  bot.send_message(message.chat.id, 'выбирите один из цветов заливки заднего фона(у робота):\nк командам -> "/comms"', reply_markup=chbg)
@bot.message_handler(commands=['assis_msgs_onoff'])
def onoff(message):
  global on_off
  if on_off == True:
    on_off = False
    bot.send_message(message.chat.id, 'вспомогающих сообщений не будет, для включения их обратно -> "/assis_msgs_onoff"\nк командам -> "/comms"')
  else:
    on_off = True
    bot.send_message(message.chat.id, 'вспомогающие сообщения будут появлятся, для их выключения -> "/assis_msgs_onoff"\nк командам -> "/comms"')
@bot.message_handler(commands=['code'])
def code(message):
    txt=['from m5stack import *',
    'from m5ui import *',
    'from uiflow import *',
    'import unit',
    'import machine',
    'from m5mqtt import M5mqtt as q',
    'setScreenColor(0xa7ff00)',
    'l0 = M5TextBox(148, 69, "};3", lcd.FONT_DejaVu72, 0x5400f5, rotate=90)',
    'l = M5TextBox(119, 29, "SEvaORG©", lcd.FONT_Comic, 0xff0400, rotate=0)',
    "w = q('m5stack','broker.hivemq.com',1883,'','',300)",
    'm =module.get(module.BASE_X)',
    'rg= unit.get(unit.RGB, unit.PORTB)',
    'rg.setColorAll(0xffe5b4)',
    "def comms(topic_data):",
      "    if topic_data=='stright':",
        '        m.set_motor_speed(2, 90)',
        '        m.set_motor_speed(1, 90)',
        '        wait_ms(1000)',
        '        m.set_motor_speed(2, 0)',
        '        m.set_motor_speed(1, 0)',
      "    elif topic_data=='re':",
        '        l.setColor(0xffff00)',
        '        l0.setColor(0x5400f5)',
        '        setScreenColor(0xff0000)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='or':",
        '        l.setColor(0xff0400)',
        '        l0.setColor(0x5400f5)',
        '        setScreenColor(0xff8700)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='ye':",
        '        l.setColor(0xff0400)',
        '        l0.setColor(0x5400f5)',
        '        setScreenColor(0xffff00)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='gr':",
        '        l.setColor(0xff0400)',
        '        l0.setColor(0x5400f5)',
        '        setScreenColor(0x00ff33)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='cy':",
        '        l.setColor(0xff0400)',
        '        l0.setColor(0x5400f5)',
        '        setScreenColor(0x00ffe2)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='bl':",
        '        l.setColor(0xff0400)',
        '        l0.setColor(0xff0000)',
        '        setScreenColor(0x2c00ff)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='pu':",
        '        l.setColor(0xff0400)',
        '        l0.setColor(0xff0000)',
        '        setScreenColor(0xdb00ff)',
        '        l.show()',
        '        l0.show()',
      "    elif topic_data=='stright2':",
        '        m.set_motor_speed(2, 90)',
        '        m.set_motor_speed(1, 90)',
        '        wait_ms(7000)',
        '        m.set_motor_speed(2, 0)',
        '        m.set_motor_speed(1, 0)',
      "    elif topic_data=='behind':",
        '        m.set_motor_speed(2, -90)',
        '        m.set_motor_speed(1, -90)',
        '        wait_ms(1000)',
        '        m.set_motor_speed(2, 0)',
        '        m.set_motor_speed(1, 0)',
      "    elif topic_data=='right':",
        '        m.set_motor_speed(1, 90)',
        '        m.set_motor_speed(2, -90)',
        '        wait_ms(500)',
        '        m.set_motor_speed(1, 0)',
        '        m.set_motor_speed(2, 0)',
      "    elif topic_data=='left':",
        '        m.set_motor_speed(2, 90)',
        '        m.set_motor_speed(1, -90)',
        '        wait_ms(500)',
        '        m.set_motor_speed(2, 0)',
        '        m.set_motor_speed(1, 0)',
      '    elif topic_data == "honkers":',
        '        for i in range(30):',
          '            rg.setColorAll(0xff0000)',
          '            wait_ms(1)',
          '            speaker.sing(147, 1/4)',
          '            rg.setColorAll(0x222222)',
         '            wait_ms(100)',
      '    elif topic_data == "reboot":',
        '        machine.reset()',
    'w.subscribe(str("testopic/2"), comms)',
    'w.start()']
    text228 = '\n'.join(txt)
    bot.reply_to(message, '# а вот и он!:\n\n'+text228+'\n\n# а теперь скопируйте его и вставьте сюда:"https://flow.m5stack.com/", перейдите во вкладку "</>python", вставьте код и после нажмите кнопку "run" (ничего не удалять не надо) и перейдите в телеграмм.После этих действий пропишите комманду "/comms", и управляйте им на здоровье.(!ЕСЛИ В М5 ПОПРОСЯТ КОД ТО ВВЕДИТЕ: D58D8813!)(SEvaORG©)' )
'''@bot.message_handler(commands=['chSm'])
def chSm(message):
  chsm= ty.InlineKeyboardMarkup(row_width=1)
  q1 =  ty.InlineKeyboardButton('красный', callback_data='re')
  q2 =  ty.InlineKeyboardButton('оранжевый', callback_data='or')
  q3 =  ty.InlineKeyboardButton('желтый', callback_data='ye')
  q4 =  ty.InlineKeyboardButton('зеленый', callback_data='gr')
  q5 =  ty.InlineKeyboardButton('голубой', callback_data='cy')
  q6 =  ty.InlineKeyboardButton('синий', callback_data='bl')
  q7 =  ty.InlineKeyboardButton('фиолетовый', callback_data='pu')'''
@bot.callback_query_handler(func=lambda call:True)
def call1(call):
    if call.message:
        if call.data == 'stra':
            m5.publish('testopic/2', 'stright')
            print('(/прямо)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/прямо)✅sucess(ive sent da command)')
        if call.data == 'str':
            m5.publish('testopic/2', 'stright2')
            print('(/прямо(долго))✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/прямо(долго))✅sucess(ive sent da command)')
        elif call.data == 'beh':
            m5.publish('testopic/2', 'behind')
            print('(/назад)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/назад)✅sucess(ive sent da command)')
        elif call.data == 'lef':
            m5.publish('testopic/2', 'left')
            print('(/направо)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/направо)✅sucess(ive sent da command)')
        elif call.data == 'rig':
            m5.publish('testopic/2', 'right')
            print('(/налево)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/налево)✅sucess(ive sent da command)')
        elif call.data == 'hor':
            m5.publish('testopic/2', 'honkers')
            print('(/громкий_гудок)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/громкий_гудок)✅sucess(ive sent da command)')
        elif call.data == 'reb':
            m5.publish('testopic/2', 'reboot')
            print('(/перезагрузка)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/перезагрузка)✅sucess(ive sent da command)')
        elif call.data == 're':
            m5.publish('testopic/2', 're')
            print('(/установлен фон:красный)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:красный)✅sucess(ive sent da command)')
        elif call.data == 'or':
            m5.publish('testopic/2', 'or')
            print('(/установлен фон:оранжевый)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:оранжевый)✅sucess(ive sent da command)')
        elif call.data == 'ye':
            m5.publish('testopic/2', 'ye')
            print('(/установлен фон:желтый)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:желтый)✅sucess(ive sent da command)')
        elif call.data == 'gr':
            m5.publish('testopic/2', 'gr')
            print('(/установлен фон:зеленый)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:зеленый)✅sucess(ive sent da command)')
        elif call.data == 'cy':
            m5.publish('testopic/2', 'cy')
            print('(/установлен фон:голубой)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:голубой)✅sucess(ive sent da command)')
        elif call.data == 'bl':
            m5.publish('testopic/2', 'bl')
            print('(/установлен фон:синий)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:синий)✅sucess(ive sent da command)')
        elif call.data == 'pu':
            m5.publish('testopic/2', 'pu')
            print('(/установлен фон:фиолетовый)✅sucess(ive sent da command)')
            if on_off == True:
              bot.send_message(call.message.chat.id, '(/установлен фон:фиолетовый)✅sucess(ive sent da command)')
bot.infinity_polling()
m5.loop_forever()
