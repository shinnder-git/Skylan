####################

import ctypes # System
import os # System
import time # System
import json # System
import random # System
import webbrowser # System

####################

# pip install plyer
from plyer import notification

# pip install keyboard
import keyboard

# pip install kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# pip install kivymd
from kivymd.app import MDApp
from kivy.config import Config

####################


class HelloScreen(Screen):
	def on_enter(self, *args):
		Clock.schedule_once(self.switch_to_home, 5)

	def switch_to_home(self, dt):
		self.manager.current = 'main'

class MainScreen(Screen):
	pass

class SkylanApp(MDApp):
	def build(self):
		global notification_check

		notification_check = True

		users = get_users()
		name = os.environ.get('USERNAME')


		self.theme_cls.theme_style = users[str(name)]['theme']
		self.icon = 'img/skylan.png'
		self.theme_cls.primary_palette = "Amber"
		self.theme_cls.accent_palette = "Amber"

		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Skylan')
		Config.set('kivy', 'window_icon', 'img/skylan.png')
		Builder.load_file('app.kv')

		sm = ScreenManager()
		sm.add_widget(HelloScreen(name='hello'))
		sm.add_widget(MainScreen(name='main'))

		return sm

	def restart(self):
		self.root.clear_widgets()
		self.stop()
		return SkylanApp().run()

	def spam(self):
		text = self.root.get_screen('main').ids.spam_text.text
		amount = self.root.get_screen('main').ids.amount.text
		interval = self.root.get_screen('main').ids.interval.text
		if notification_check == True:
			notification.notify(
				title='Skylan',
				message='Работа начнеться через 5 секунд.\nНажмите на поле с текстом.',
				app_name='Skylan',
				app_icon='img/skylan.ico'
			)
		else:
			pass
		time.sleep(5)
		for i in range(int(amount)):
			time.sleep(int(interval))
			keyboard.write(text)
			keyboard.press('enter')

		if notification_check == True:
			notification.notify(
				title='Skylan',
				message='Работа закончина.',
				app_name='Skylan',
				app_icon='img/skylan.ico'
				)
		else:
			pass

		return

	def ghoul(self):
		ghoul = 1000
		interval = self.root.get_screen('main').ids.interval.text
		if notification_check == True:
			notification.notify(
				title='Skylan',
				message='Работа начнеться через 5 секунд.\nНажмите на поле с текстом.',
				app_name='Skylan',
				app_icon='img/skylan.ico'
			)
		else:
			pass
		time.sleep(5)
		while ghoul	> 7:
			time.sleep(int(interval))
			keyboard.write(f"{ghoul}-7={ghoul-7}")

			keyboard.press('enter')
			ghoul -= 7

		keyboard.write("Im Ghoul...")
		keyboard.press('enter')
		if notification_check == True:
			notification.notify(
				title='Skylan',
				message='Работа закончина.',
				app_name='Skylan',
				app_icon='img/skylan.ico'
				)
		else:
			pass

		return

	def random_fuck(self):
		with open('data/obscene language.json', encoding='utf-8') as file:
			fuck = json.load(file)
		if notification_check == True:
			notification.notify(
				title='Skylan',
				message='Работа начнеться через 5 секунд.\nНажмите на поле с текстом.',
				app_name='Skylan',
				app_icon='img/skylan.ico'
			)
		else:
			pass
		amount = self.root.get_screen('main').ids.amount.text
		interval = self.root.get_screen('main').ids.interval.text
		time.sleep(5)

		for i in range(int(amount)):
			time.sleep(int(interval))
			word = random.choice(fuck['obscene language'])

			keyboard.write(word)
			keyboard.press('enter')
		if notification_check == True:
			notification.notify(
				title='Skylan',
				message='Работа закончина.',
				app_name='Skylan',
				app_icon='img/skylan.ico'
				)
		else:
			pass

		return

	def donate(self):
		webbrowser.open_new("https://www.donationalerts.com/r/anliro")

	def github(self):
		webbrowser.open_new('https://github.com/anliro-dev/Skylan.git')

	def telegram(self):
		webbrowser.open_new('https://t.me/skylan_spam')



	def notifications_check(self, checkbox, value):
		if value:
			notification_check = True
		else:
			notification_check = False

	def themes_check(self):
		with open(f"./data/user.json", encoding='utf-8') as file:
			global user
			user = json.load(file)
		name = os.environ.get('USERNAME')

		if user[str(name)]['theme'] == "Light":
			user[str(name)]['theme'] = 'Dark'
			self.theme_cls.theme_style = user[str(name)]['theme']
			Builder.load_file('app.kv')
		else:
			user[str(name)]['theme'] = 'Light'
			self.theme_cls.theme_style = user[str(name)]['theme']
			Builder.load_file('app.kv')

		with open('./data/user.json', 'w', encoding='utf-8') as file:
			return json.dump(user, file, indent=4, sort_keys=True,ensure_ascii=True)


####################

def get_users():
	with open('data/user.json', 'r', encoding='utf-8') as f:
		users = json.load(f)

	return users

def open_account():
	users = get_users()
	name = os.environ.get('USERNAME')
	version_skylan = 0.7

	if str(name) in users:
		return False
	else:
		users[str(name)] = {}
		users[str(name)]['theme'] = 'Dark'
		users[str(name)]['version'] = version_skylan

	with open('./data/user.json', 'w', encoding='utf-8') as file:
		return json.dump(users, file, indent=4, sort_keys=True, ensure_ascii=True)


###################

if __name__ == '__main__':
	open_account()
	SkylanApp().run()