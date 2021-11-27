#beta 0.5
#Link on bot: @newloveubot or t.me/newloveubot
#Link on me: https://github.com/henmasta

""" 
Будь осторожен, странник.
Это "приложение" для бота сделано из говна и говна. 
Если ты дотронешься до него, то твоя честь больше никогда не будет отмыта.
"""

import os
import sys
import time
import telebot
import threading
import tkinter as tk
import win32gui, win32con
from tkinter import Label
from tkinter import Button
from tkinter import messagebox

#Get Telegram token
bot = telebot.TeleBot("2100347098:AAE66dt074ywIrXyJ_7mIsG68vGWjtoiZpU")

#Function for button "START"
def start(self):
	messagebox.showinfo('ОНО ЖИВОЕ!!!', 'Бот запущен и работает!')
	start_text = Label(root, text = "Status: ОН ЖИВЕТ!!!", fg = "green", font=("Verdana 35	 bold"))
	start_text.pack(pady = 30)
	@bot.message_handler(commands=['Start', 'start'])
	def send_welcome(message):
		bot.reply_to(message, 'Напиши "/люблю" и увидишь действие))')

	@bot.message_handler(commands=['люблю', 'Люблю'])
	def love(message):
		bot.reply_to(message, "Всего 30 раз))")
		i = 0
		while(i <= 30):
			time.sleep(1)
			bot.reply_to(message, "Люблю💜💜💜")
			print(i)
			i += 1

	bot.infinity_polling()

#Function for button "EXIT"
def exit():
	os._exit(0)

#Interface field declaration
root = tk.Tk()
root.title("Bot")

text_label = "Нажми старт чтобы начать\n\nBыйти чтобы выйти))"

_label = Label(root, text = text_label, font=("Arial Bold", 20))
_label.pack(pady = 50)

_thread = threading.Thread(target = start, args = (1,))

#Buttons
_button_run = Button(root, text = "START", bg = "green", font=('Arial', 24), command = _thread.start)
_button_exit = Button(root, text = "EXIT", bg = "red", font=('Arial', 24), command = exit)

_button_run.place(x = 100, y = 360)
_button_exit.place(x = 400, y = 360)


if __name__ == "__main__":
	_hide = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(_hide , win32con.SW_HIDE)
	root.geometry('600x500')
	root.resizable(False, False)
	root.mainloop()