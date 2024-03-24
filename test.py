from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import random
import time
import threading
import asyncio

#Глобальные настройки
Window.title = "Игра"
Window.size = (350, 650)
Window.clearcolor = (0, 0, 0, 1)

ivent = [
	"Вы нашли\nсундук", 
	"На вас напали\nбандиты", 
	"Вы нашли\nдеревню", 
	"Вы нашли\nдракона", 
	"На вас\nнапали волки", 
	"Вы напаролись на\n ржавый гвоздь",
	"Вы нашли\n подорожник"
	]

#ivent = ["На вас напали\nбандиты", "На вас\nнапали волки"]

start_string = "Куда идём?"
menu_batle_idle_text = "Атаковать"

class Player():
	LIFE = 100
	IDLE = 0
	RUN = 2
	BATLE = 1
	PLAYER_BATLE = 1.1
	ENEMY_BATLE = 1.2
	DEAD = 3

	def attaсk():
		damage = [ 2, 5, 10 ]
		#random.shuffle(damage)
		rnd = random.choice(damage)
		EnemyNps.LIFE -= rnd
		return rnd

class EnemyNps():
	LIFE = 100

	def attack():
		damage = [ 1, 3, 5 ]
		#random.shuffle(damage)
		rnd = random.choice(damage)
		Player.LIFE -= rnd
		return rnd

class Items():
	PLANTAIN = 10

class MyApp(App):

	grid = GridLayout(cols=1)
	current_widgets = set()
	player_state = Player.IDLE

	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()

	def build(self):
		start_button = Button(text="Начать путишествие", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1), font_name="press-start-2p-regular")
		start_button.bind(on_press=self.main_loop_)
		self.grid.add_widget(start_button)
		self.current_widgets.add(start_button)
		
		return self.grid

	def add_widgetttt(self, w):
		self.grid.add_widget(w)
		self.current_widgets.add(w)

	#Меню движения
	def menu(self, txt):
		box1 = BoxLayout(orientation='horizontal', size_hint_y=None)
		box2 = BoxLayout()
		box3 = BoxLayout(orientation='vertical')
		label_hp = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		#label_mn = Label(text="100 mn", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		label_ivent = Label(text=start_string, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		button11 = Button(text="Идти налево", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button11.bind(on_press=self.run_ivent)
		button12 = Button(text="Идти направо", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button12.bind(on_press=self.run_ivent)
		box1.add_widget(label_hp)
		#box1.add_widget(label_mn)
		box2.add_widget(label_ivent)
		box3.add_widget(button11)
		box3.add_widget(button12)
		self.add_widgetttt(box1)
		self.add_widgetttt(box2)
		self.add_widgetttt(box3)

	#Меню выбора битвы
	def menu_batle(self, txt):
		box1 = BoxLayout(orientation='horizontal', size_hint_y=None)
		box2 = BoxLayout()
		box3 = BoxLayout(orientation='vertical')
		label_hp = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		#label_mn = Label(text="100 mn", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		label_ivent = Label(text=start_string, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		button11 = Button(text="Начать битву", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button11.bind(on_press=self.start_batle)
		button12 = Button(text="Бежать", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button12.bind(on_press=self.run_away)
		box1.add_widget(label_hp)
		#box1.add_widget(label_mn)
		box2.add_widget(label_ivent)
		box3.add_widget(button11)
		box3.add_widget(button12)
		self.add_widgetttt(box1)
		self.add_widgetttt(box2)
		self.add_widgetttt(box3)

	#Меню битвы
	def menu_batle_idle_player(self, txt):
		box1 = BoxLayout(orientation='horizontal', size_hint_y=None)
		box2 = BoxLayout()
		box3 = BoxLayout(orientation='vertical')
		label_hp = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		label_mn = Label(text=f"{EnemyNps.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		label_ivent = Label(text=start_string, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		button11 = Button(text="Атаковать", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button11.bind(on_press=self.attack_player)
		button12 = Button(text="Бежать", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		#button12.bind(on_press=self.run_away)
		box1.add_widget(label_hp)
		box1.add_widget(label_mn)
		box2.add_widget(label_ivent)
		box3.add_widget(button11)
		box3.add_widget(button12)
		self.add_widgetttt(box1)
		self.add_widgetttt(box2)
		self.add_widgetttt(box3)

	def menu_batle_idle_enemy(self, txt):
		box1 = BoxLayout(orientation='horizontal', size_hint_y=None)
		box2 = BoxLayout()
		box3 = BoxLayout(orientation='vertical')
		label_hp = Label(text=f"{Player.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		label_mn = Label(text=f"{EnemyNps.LIFE} hp", font_size=30, size_hint=(None, None), size=(350, 100), pos_hint=({'top': 1}), font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		label_ivent = Label(text=start_string, halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
		button11 = Button(text="Ход противника", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		button11.bind(on_press=self.attack_enemy)
		#button12 = Button(text="Бежать", font_name="press-start-2p-regular", background_color=(1, 0, 0, 1), color=(0, 1, 0, 1))
		#button12.bind(on_press=self.run_away)
		box1.add_widget(label_hp)
		box1.add_widget(label_mn)
		box2.add_widget(label_ivent)
		box3.add_widget(button11)
		#box3.add_widget(button12)
		self.add_widgetttt(box1)
		self.add_widgetttt(box2)
		self.add_widgetttt(box3)

	#Функция статуса при путишествии игрока
	def main_loop_(self, *args, **kwargs):
		print(self, args, kwargs)
		print(self.current_widgets)
		for w in list(self.current_widgets):
			self.current_widgets.remove(w)
			self.grid.remove_widget(w)
		if (self.player_state == Player.IDLE):
			self.menu(start_string)
		elif (self.player_state == Player.RUN):
			label = Label(text="strng", halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			self.add_widgetttt(label)
		elif (self.player_state == Player.BATLE):
			self.menu_batle(start_string)
		elif (self.player_state == Player.PLAYER_BATLE):
			self.menu_batle_idle_player(start_string)
		elif (self.player_state == Player.ENEMY_BATLE):
			self.menu_batle_idle_enemy(start_string)
		elif (self.player_state == Player.DEAD):
			label = Label(text="Конец игры", halign="center", font_size=30, font_name="press-start-2p-regular", color=(0, 1, 0, 1))
			self.add_widgetttt(label)


	def run_away(self, *args):
		escape = escape = [ False, True ]
		rnd = random.choice(escape)
		if (rnd == False):
			self.start_batle()
		elif (rnd == True):
			global start_string
			start_string="Побег удался\nКуда идти?"
			self.player_state = Player.IDLE
			self.main_loop_()

	def start_batle(self, *args):
		global start_string
		start_string="Начало битвы"
		self.player_state = Player.PLAYER_BATLE
		self.main_loop_()

	def attack_player(self, *args):
		info = Player.attaсk()
		global start_string
		start_string=f"Вы нанесли {info}\nурона"
		if (Player.LIFE <= 0):
			self.player_state = Player.DEAD
			self.main_loop_()
		elif (EnemyNps.LIFE <= 0):
			self.player_state = Player.IDLE
			start_string = "Победа!\nКуда идём"
			EnemyNps.LIFE = 100
			self.main_loop_()
		else:
			self.player_state = Player.ENEMY_BATLE
			self.main_loop_()
		

	def attack_enemy(self, *args):
		info = EnemyNps.attack()
		global start_string
		start_string=f"Вам нанесли {info}\nурона"
		if (Player.LIFE <= 0):
			self.player_state = Player.DEAD
			self.main_loop_()
		elif (EnemyNps.LIFE <= 0):
			self.player_state = Player.IDLE
			start_string = "Победа!\nКуда идём"
			EnemyNps.LIFE = 100
			self.main_loop_()
		else:
			self.player_state = Player.PLAYER_BATLE
			self.main_loop_()

	def run_ivent(self, *args):
		global start_string
		def rnd_ivent(*args):
			random.shuffle(ivent)
			rnd = random.choice(ivent)
			global start_string
			if (start_string == rnd):
				random.shuffle(ivent)
				rnd = random.choice(ivent)
				return rnd
			else:
				return rnd

		#if (start_string == "Вы напаролись на\n ржавый гвоздь"):
		#	Player.LIFE -= 10
		#elif (start_string == "Вы нашли\n подорожник"):
		#	Player.LIFE += 10

		if (start_string == "На вас напали\nбандиты"):
			start_string = "Что делать?"
			self.player_state = Player.BATLE
			self.main_loop_()
		else:
			start_string = rnd_ivent()
			self.player_state = Player.IDLE
			self.main_loop_()

		#self.menu(rnd_ivent())
		#self.player_state = Player.IDLE
		#self.main_loop_()

	'''
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
	'''
# Запуск проекта
if __name__ == "__main__":
	MyApp().run()
