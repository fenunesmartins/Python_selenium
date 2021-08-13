from selenium import webdriver
import os
from time import sleep
url = "https://www.coronatracker.com/pt-br/"

scrap = webdriver.Chrome()
scrap.get(url)

sleep(5)
curados = scrap.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
mortos = scrap.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')
confirmados = scrap.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')

curadostext = curados.text
mortostext = mortos.text
confirmadostext = confirmados.text

print(f'Curados: {curadostext}')
print(f'Mortos: {mortostext}')
print(f'Confirmados: {confirmadostext}')

with open('dados.txt', 'w') as arquivo:
    arquivo.write(curadostext)
    arquivo.write(mortostext)
    arquivo.write(confirmadostext)

