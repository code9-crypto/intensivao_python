#Importando biblioteca que fará a execução automática e a biblioteca para usar o tempo
import pyautogui as auto
import time
import pandas as pd

#Pausando os comandos a cada 1 segundo
auto.PAUSE = 1

#Executando a sequência para entrar no navegador
auto.hotkey("win","d")
auto.click(x=31, y=446, clicks=2)

#Este tempo irá aguardar 5 segundos até o navegador abrir
time.sleep(5)

#Executando a sequência para entrar no link e fazer o login na página
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
auto.write(link)
auto.press("enter")

#Aqui irá aguardar 5 até a página ser carregada
time.sleep(5)

#dando continuidade ao login
auto.click(x=844, y=413)
auto.write("convidadoc38@gmail.com")
auto.press("tab")
auto.write("123456")
auto.press("tab")
auto.press("enter")

#extraindo as informações do arquivo csv
tabela = pd.read_csv("produtos.csv")

time.sleep(5)
#pegando cada informação da variável tabela e inserindo os dados no sistema
for linha in tabela.index:
    #clicando no primeiro campo do sistema
    auto.click(x=809, y=246)
    #pegando o valor da célula mediante o índice e coluna
    codigo = tabela.loc[linha, "codigo"]
    auto.write(str(codigo))
    auto.press("tab")
    marca = tabela.loc[linha, "marca"]
    auto.write(str(marca))
    auto.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    auto.write(str(tipo))
    auto.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    auto.write(str(categoria))
    auto.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]
    auto.write(str(preco))
    auto.press("tab")
    custo = tabela.loc[linha, "custo"]
    auto.write(str(custo))
    auto.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        auto.write(str(obs))
    auto.press("tab")
    auto.press("enter")
    auto.scroll(500)
