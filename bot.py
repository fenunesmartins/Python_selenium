import pyautogui
import time

#pyautogui.PAUSE = 1.5

#abrir a ferramenta/sistema/programa/escrever no excel
#pyautogui.press("win")
#pyautogui.write("excel")
#pyautogui.press("enter")
#pyautogui.press("enter")

#time.sleep(3)

#pyautogui.click(x=2240, y=375)
#pyautogui.write('Automatizando processo')

#pyautogui.click(x=2241, y=396)
#pyautogui.write('1')

# pyautogui.position() usei pra decobrir o pixel na tela

#abrir navegador e digitar dados de acesso

from selenium import webdriver
navegador = webdriver.Chrome()

navegador.get('https://login.live.com/')
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys('teste@teste.com')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys('senha')
