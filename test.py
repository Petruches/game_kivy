from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import random
import time
#import getch
#import click
#import clock
import threading
import asyncio

#Глобальные настройки
Window.title = "Игра"
Window.size = (350, 650)
Window.clearcolor = (0, 0, 0, 1)

#ivent = ["Вы нашли\nсундук", "На вас напали\nбандиты", "Вы нашли\nдеревню", "Вы нашли\nдракона", "На вас\nнапали волки"]
ivent = ["На вас напали\nбандиты", "На вас\nнапали волки"]
#hp = 100
enemy_battle = False
strng = "Куда идём?"

box1 = BoxLayout(orientation='horizontal', size_hint=(None, 1))
box2 = BoxLayout(orientation='vertical')
box3 = BoxLayout(orientation='horizontal')
gridox2 = GridLayout(cols=2)

def start(self):
	self.label = Label(text=strng, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
	self.label1 = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
	self.label2 = Label(text="100 mn", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
	#self.button1 = Button(text="Кнопка", size_hint=(None, None), size=(350, 100), font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
	#self.button2 = Button(text="Кнопка", size_hint=(None, None), size=(350, 100), font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
	self.button11 = Button(text="Кнопка11", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
	self.button12 = Button(text="Кнопка12", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
	self.button13 = Button(text="Кнопка13", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
	self.button14 = Button(text="Кнопка14", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
	#self.button1.bind(on_press=self.tst)
	#self.button2.bind(on_press=self.tst2)
	self.button11.bind(on_press=self.tst)
	#self.button12.bind(on_press=self.tst2)
	self.button13.bind(on_press=self.callback)
	self.button14.bind(on_press=self.att)


class Player():
	LIFE = 100
	IDLE = 0
	BATTLE = 1
	RUN = 2

class MyApp(App):

	grid = GridLayout(cols=1)
	current_widgets = set()
	player_state = Player.IDLE

	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		#start(self)

	def build(self):
		##box = BoxLayout(orientation='vertical')
		##box4 = BoxLayout(orientation='horizontal')

		#box1 = BoxLayout(orientation='horizontal', size_hint=(None, 1))
		##box1.add_widget(self.label1)
		##box1.add_widget(self.label2)

		#box2 = BoxLayout(orientation='vertical')
		##box2.add_widget(self.label)

		#box3 = BoxLayout(orientation='horizontal')
		#box3.add_widget(self.button1)
		#box3.add_widget(self.button2)
		##gridox2.add_widget(self.button11)
		##gridox2.add_widget(self.button12)
		##gridox2.add_widget(self.button13)
		##gridox2.add_widget(self.button14)

		##box.add_widget(box1)
		##box.add_widget(box2)
		#box.add_widget(box3)
		##box.add_widget(gridox2)
		start_button = Button(text="Начать путишествие", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1), font_name="press-start-2p-regular")
		start_button.bind(on_press=self.main_loop_)
		self.grid.add_widget(start_button)
		self.current_widgets.add(start_button)
		return self.grid

	def add_widgetttt(self, w):
		self.grid.add_widget(w)
		self.current_widgets.add(w)

	def menu(self):
		label = Label(text="Вы гуляли и натолкнулись на врага")
		fight_button = Button(text="Драться", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		run_button = Button(text="Убежать", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		self.add_widgetttt(label)
		self.add_widgetttt(fight_button)
		self.add_widgetttt(run_button)

	def menu2(self):
		#box2 = BoxLayout(orientation='vertical')
		#box3 = BoxLayout(orientation='horizontal')
		label1 = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		#label2 = Label(text="100 mn", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		#box2.add_widget(label1)
		label = Label(text=strng, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		button11 = Button(text="Бежать налево", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button12 = Button(text="Бежать направо", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		#self.add_widgetttt(box2)
		#self.add_widget(box3)
		self.add_widgetttt(label1)
		#self.add_widgetttt(label2)
		self.add_widgetttt(label)
		self.add_widgetttt(button11)
		self.add_widgetttt(button12)
		button11.bind(on_press=self.tst)


	def main_loop_(self, *args, **kwargs):
		print(self, args, kwargs)
		print(self.current_widgets)
		for w in list(self.current_widgets):
			self.current_widgets.remove(w)
			self.grid.remove_widget(w)
		if (self.player_state == Player.IDLE):
			label1 = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			label = Label(text=strng, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			button11 = Button(text="Бежать налево", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
			button12 = Button(text="Бежать направо", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
			self.add_widgetttt(label1)
			self.add_widgetttt(label)
			self.add_widgetttt(button11)
			self.add_widgetttt(button12)
			button11.bind(on_press=self.tst)
		elif (self.player_state == Player.RUN):
			label = Label(text="strng", halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			self.add_widgetttt(label)
	
	def running(self, *args):
		self.player_state = Player.RUN
		self.main_loop_()

	def tst(self, *args, **kwargs):
		#box1.remove_widget(self.label2)
		random.shuffle(ivent)
		rnd = random.choice(ivent)
		print(rnd)
		global strng

		if (strng == rnd):
			random.shuffle(ivent)
			rnd = random.choice(ivent)
			strng = rnd
			print(strng)

			label1 = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			label = Label(text=strng, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			button11 = Button(text="Бежать налево", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
			button12 = Button(text="Бежать направо", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
			self.add_widgetttt(label1)
			self.add_widgetttt(label)
			self.add_widgetttt(button11)
			self.add_widgetttt(button12)

			self.main_loop_()
			#label.text = strng
		else:
			strng = rnd
			print(strng)

			label1 = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			label = Label(text=strng, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			button11 = Button(text="Бежать налево", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
			button12 = Button(text="Бежать направо", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
			self.add_widgetttt(label1)
			self.add_widgetttt(label)
			self.add_widgetttt(button11)
			self.add_widgetttt(button12)

			self.main_loop_()

		#if (strng == "На вас напали\nбандиты"):
		#	print("F")


	def att(self, *args, **kwargs):
		strng = "Вы ударили"
		self.label.text = strng
		print(strng)
		#self.label.text = "Вы ударили"
		print(f"'{self.label.text}'", self.label.text == "Вы ударили")


	def callback(self, *args, **kwargs):
		strng = "гг изи\nхыхы"
		self.label.text = strng
		print(strng)
		#self.label.text = "гг изи\nхыхы"
		print(self.label.text)

	def tst2(self, *args, **kwargs):
		box1.add_widget(self.label2)#сразу не нажимать, вылетает баг
		global hp
		hp=hp-1
		print(hp)
		self.label1.text = f"{hp} hp"

# Запуск проекта
if __name__ == "__main__":
	MyApp().run()
