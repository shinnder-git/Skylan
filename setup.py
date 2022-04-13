import os

list = ['Kivy==2.1.0', 'keyboard==0.13.5', 'kivymd==0.104.2', 'plyer==2.0.0']

for item in list:
	os.system(f"pip install {item}")

print('Все загружено.')