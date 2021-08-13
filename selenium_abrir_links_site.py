# Utilizando o webdriver do selenium para conectar ao site usando o webdriver do crohme

from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://itupeva.sp.gov.br")
navegador.find_element_by_xpath('//*[@id="site-nav-trigger"]/ul/li[4]/a').click() #clicando no link notícias, pelo xpath
navegador.find_element_by_xpath('//*[@id="conteudo"]/section/div/div/main/div/article[1]/div/h3/a').click() #escolhendo uma notícia pelo xpath
