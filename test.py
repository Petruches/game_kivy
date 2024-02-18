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
hp = 100
enemy_battle = False

box1 = BoxLayout(orientation='horizontal', size_hint=(None, 1))
box2 = BoxLayout(orientation='vertical')
box3 = BoxLayout(orientation='horizontal')
gridox2 = GridLayout(cols=2)

def start(self):
	self.label = Label(text="Вы погибли", halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
	self.label1 = Label(text=f"{hp} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
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


class MyApp(App):

	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		start(self)

	def build(self):
		box = BoxLayout(orientation='vertical')
		box4 = BoxLayout(orientation='horizontal')

		#box1 = BoxLayout(orientation='horizontal', size_hint=(None, 1))
		box1.add_widget(self.label1)
		box1.add_widget(self.label2)

		#box2 = BoxLayout(orientation='vertical')
		box2.add_widget(self.label)

		#box3 = BoxLayout(orientation='horizontal')
		#box3.add_widget(self.button1)
		#box3.add_widget(self.button2)
		gridox2.add_widget(self.button11)
		gridox2.add_widget(self.button12)
		gridox2.add_widget(self.button13)
		gridox2.add_widget(self.button14)

		box.add_widget(box1)
		box.add_widget(box2)
		#box.add_widget(box3)
		box.add_widget(gridox2)
		return box


	def tst(self, *args, **kwargs):
		box1.remove_widget(self.label2)
		random.shuffle(ivent)
		rnd = random.choice(ivent)
		
		if (self.label.text == rnd):
			random.shuffle(ivent)
			rnd = random.choice(ivent)
			self.label.text = rnd
		else:
			self.label.text = rnd

		if (self.label.text == "На вас напали\nбандиты"):
			self.button11.disabled = True
			self.button12.disabled = True
			self.bitva(self)
			print("F")


	async def bitva(self, *args, **kwargs):
		sss=True
		while(sss):
			if (self.label.text == "Вы ударили"):
				await asyncio.sleep(2)
				print(f"'{self.label.text}'", self.label.text == "Вы ударили")
				print("Нанесен удар по нпс")
				self.button11.disabled = False
				self.button12.disabled = False
				sss=False
				break
			elif (self.label.text == "Вы промахнулись"):
				await asyncio.sleep(2)
				print(self.label.text)
				await print("Пропуск хода")
				self.button11.disabled = False
				self.button12.disabled = False
				sss=False
				break

	def att(self, *args, **kwargs):
		self.label.text = "Вы ударили"
		print(f"'{self.label.text}'", self.label.text == "Вы ударили")


	def callback(self, *args, **kwargs):
		self.label.text = "гг изи\nхыхы"
		print(self.label.text)

	def tst2(self, *args, **kwargs):
		box1.add_widget(self.label2)#сразу не нажимать, вылетает баг
		global hp
		hp=hp-1
		print(hp)
		self.label1.text = f"{hp} hp"
'''
	def battle(self, *args, **kwargs):
		self.button11.disabled = True
		self.button12.disabled = True
		
		sss=True
		global battle
		global hp
		enemy_battle = True
		enemy_nps_hp=100
		enemy_ivent = ["Удар", "Мимо"]
		my_ivent = ["Удар", "Мимо"]

		while enemy_nps_hp != 0:
			random.shuffle(enemy_ivent)
			enemy_rnd = random.choice(enemy_ivent)

			self.label.text = enemy_rnd
			if (enemy_rnd == "Удар"):
				hp=hp-10
				self.label1.text = f"{hp} hp"
			elif (enemy_rnd == "Мимо"):
				self.label.text == "Мимо"
			print("Должен быть твой ход")
			#while(sss):
				#self.button13.on_press

	def but1(self, *args, **kwargs):
			print("dsa")
'''

# Запуск проекта
if __name__ == "__main__":
	MyApp().run()
