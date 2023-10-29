#importando bibliotecas que fará a automação
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


#abrindo o navegador edge e aguarda 5 segundos para esperar o navegador abrir
navegador = webdriver.Edge()
time.sleep(5)

#entrando no link e aguarda 5 segundos para esperar a página abrir
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(3)

#selecionando e preenchendo os campo de login e senha e entrando no sistema
navegador.find_element(By.XPATH,'//*[@id="email"]').send_keys("convidadoc38@gmail.com")
navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("123456")
navegador.find_element(By.XPATH,'//*[@id="pgtpy-botao"]').click()
time.sleep(5)

#extraindo informações do arquivo excel
tabela = pd.read_csv("produtos.csv")

#percorrendo os dados e inserindo nos campos
for linha in tabela.index:
    #selecionando e preenchendo os campos para cadastrar os produtos
    navegador.find_element(By.XPATH,'//*[@id="codigo"]').send_keys(str(tabela.loc[linha, 'codigo']))
    navegador.find_element(By.XPATH,'//*[@id="marca"]').send_keys(str(tabela.loc[linha, 'marca']))
    navegador.find_element(By.XPATH,'//*[@id="tipo"]').send_keys(str(tabela.loc[linha, 'tipo']))
    navegador.find_element(By.XPATH,'//*[@id="categoria"]').send_keys(str(tabela.loc[linha, 'categoria']))
    navegador.find_element(By.XPATH,'//*[@id="preco_unitario"]').send_keys(str(tabela.loc[linha, 'preco_unitario']))
    navegador.find_element(By.XPATH,'//*[@id="custo"]').send_keys(str(tabela.loc[linha, 'custo']))
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        navegador.find_element(By.XPATH, '//*[@id="obs"]').send_keys(str(tabela.loc[linha, 'obs']))
    navegador.find_element(By.XPATH,'//*[@id="pgtpy-botao"]').click()

time.sleep(3600)






