# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# class WhatsappBot:
# 	def __init__(self):
# 		self.names = ["Mae", "Bi", "Pai"]
# 		self.mensagem = "Essa mensagem foi enviada por um robô feito pelo Luan"
# 		options = webdriver.ChromeOptions()
# 		options.add_argument('lang=pt-br')
# 		self.driver = webdriver.Chrome(
# 			executable_path=r'chromedriver', chrome_options=options)

# 	def EnviarMensagens(self):
# 			self.driver.get('https://web.whatsapp.com')
# 			time.sleep(30)
# 			for name in self.names:
# 				campo_grupo = self.driver.find_element_by_xpath(f'//span[@title="{name}"]')
# 				time.sleep(3)
# 				campo_grupo.click()
# 				chat_box = self.driver.find_element_by_class_name('_13mgZ')
# 				time.sleep(3)
# 				chat_box.click()
# 				chat_box.send_keys(self.mensagem)
# 				botao_enviar = self.driver.find_element_by_xpath(
# 					"//span[@data-icon='send']")
# 				time.sleep(3)
# 				botao_enviar.click()
# 				time.sleep(5)


# bot = WhatsappBot()
# bot.EnviarMensagens()


# # -*- encoding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import time
# 
url = "https://web.whatsapp.com"
names = ["Mae", "Bi", "Pai"]
mensagem = "Essa mensagem foi enviada por um robô feito pelo Luan"
options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(executable_path=r'chromedriver', chrome_options=options)
names = ["Bi", "Mae", "Pai"]
message = "Essa mensagem foi enviada por um robô feito pelo Luan"
# 
driver.get(url)
time.sleep(10)
# 
# 
for name in names:
    search = driver.find_element_by_class_name('_2_1wd')
    time.sleep(2)
    # search.click()
    search.send_keys(name)
    print(f"Procurei {name}")
    time.sleep(10)
    person = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
    person.click()
    time.sleep(2)
    chat_box = driver.find_element_by_class_name('_2A8P4')
    time.sleep(3)
    chat_box.click()
    chat_box.send_keys(message)
    time.sleep(10)
    botao_enviar = driver.find_element_by_xpath(
        "//span[@data-icon='send']")
    time.sleep(3)
    botao_enviar.click()
    time.sleep(5)

driver.quit()