from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
import random
import time
import os


perera = os.path.abspath("./Cavaleiros/Perera.png")
luca = os.path.abspath("./Cavaleiros/Pareja.png")
didier = os.path.abspath("./Cavaleiros/Didier.png")
breno = os.path.abspath("./Cavaleiros/Breno.png")

print(perera)
print(luca)
print(didier)
print(breno)

tempo = 8

class bot:
    def __init__(self):
        self.hora = 600  #padrão é 3600
        self.sujeito = 'Rafael'
        self.tempo = 0
        self.mensagem = [f' Bill Gates, em um restaurante... Depois de comer, ele deu $5 de gorgeta. O garçom ficou olhando pra ele de forma estranha depois da gorgeta. Gates percebeu e perguntou "o que foi?" e o garçom respondeu "Eu estou impressionado porque sua filha deu uma gorgeta de $500 e você, pai dela, o homem mais rico do mundo deu somente $5?. Gates sorriu e respondeu:"Ela é filha do homem mais rico do mundo, mas eu sou o pobre filho de @{self.sujeito}'+ Keys.ENTER +f' o garoto sem foto de perfil no Zap Zap". Gates então olhou para o relógio e chorou... faltava apenas 2 horas', f'Ei @{self.sujeito}'+ Keys.ENTER +f' leon aqui. Cara na moral, tipo assim, faltam só 1 hora pro pior acontecer. Vc devia colocar essa foto de perfil logo :(']
        self.grupos = "Comecou a dentadura"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome( executable_path=r'./chromedriver.exe')
        self.cavaleiros_texto = [f'@{self.sujeito}'+Keys.ENTER+', Você desrespeitou o poder dos demônios que dominam essa terra. Seu crime não será perdoado nem pelo próprio Hittler.', f'Didier acabará com seu sofrimento @{self.sujeito}'+Keys.ENTER+'. Não há consumo de creatina que te salve das mãos dessa máquina de destruição.',f'@{self.sujeito}'+Keys.ENTER+'. Não importa o quanto que você pense em fugir de seu destino. Breno, o estrategista do submundo sempre formulará um plano para te encontrar e te destruir. Não há escapatória.',f'@{self.sujeito}'+Keys.ENTER+'. Seu caminho acaba aqui, O ADM CHEGOU E SE PASSA APENAS RAIVA E ÓDIO EM SUA MENTE. É TARDE, VOCÊ NOS TRAIU, VOCÊ FALHOU CONOSCO. MORRA.']
        self.cavaleiros = [perera,didier,breno,luca]
        self.Zero_texto = ['.','...','.........','é isto','....',f' .. @{self.sujeito}' + Keys.ENTER + ' não cumpriu seu dever dentro do tempo esperado.','........','... Em pouco tempo, haverá a reunião dos 4 demônios do apocalipse para se encarregarem das punições....','.....','..   ...... ..não há mais o que fazer.','.... nós avisamos....','....você não quis ouvir..','.......','.. ... boa sorte.']
        self.EleColocouFto_texto = '@Heitor'+ Keys.ENTER +' @Luca'+ Keys.ENTER +' @Baiano'+ Keys.ENTER +'@Breno'+ Keys.ENTER +' @Didier'+ Keys.ENTER +' @Leon'+ Keys.ENTER +' @Rafael Stolen'+ Keys.ENTER +' @Willian Alber'+ Keys.ENTER +' @Gabriel'+ Keys.ENTER +' @Lucas'+ Keys.ENTER + f'COM MUITA FELICIDADE VENHO ANUNCIAR QUE @{self.sujeito}'+ Keys.ENTER +' FINALMENTE COLOCOU UMA FOTO DE PERFIL!!!!!!! VAMOS COMEMORAR GALERAAAAAAAAA!!!!!!!!!!'

    def esperar_hora(self):
        time.sleep(self.hora)

    def EleColocouFto(self):
        #click on group
        grup = self.driver.find_element_by_xpath(f"//span[@title='{self.grupos}']")
        time.sleep(0.5)
        grup.click()

        #click on text
        caixa_texto = self.driver.find_element_by_class_name('_1Plpp')
        time.sleep(0.5)
        caixa_texto.click()
        
        #write text
        caixa_texto.send_keys(self.EleColocouFto_texto)

        #send text
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(0.5)
        botao_enviar.click()

        sys.exit()


    def verificarFto(self):
        #<div class="_3mKlI" role="button">
        #<div class="_2u2Mg">
        #<img src="https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F76663133_236463257539536_3587232954079826069_n.jpg%3Foe%3D5E8E7B91%26oh%3Deb621b847a291435d936ad5b37d46760&amp;t=s&amp;u=558496256874%40c.us&amp;i=1586019490" draggable="false" class="Qgzj8 gqwaM _3FXB1" style="visibility: visible;">
        
        #click on Rafael
        chat = self.driver.find_element_by_xpath(f"//span[@title='{self.sujeito}']")
        time.sleep(0.5)
        chat.click()

        #click to open profile
        Nome = self.driver.find_element_by_class_name('_3mKlI')
        time.sleep(0.5)
        Nome.click()

        #find photo div
        divFto = self.driver.find_element_by_class_name('_2u2Mg')
        divFto2 = divFto.find_element_by_xpath('./div[@class="_1WliW"]')
        try:
            divFto2.find_element_by_xpath('./img[@class="Qgzj8 gqwaM _3FXB1"]')
            self.EleColocouFto()
        except:
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//span[@data-icon='x']").click()
            pass


    def FinalMsgs(self):
        #<div role="button" title="Anexar">
        #<input accept="image/*,video/mp4,video/3gpp,video/quicktime" type="file" multiple="" style="display: none;">
        #<<div class="_2S1VP 
        #<span data-icon="send-light" class="">
        #### Me delete #####
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        #### Me delete #####
        for local, texto in zip(self.cavaleiros,self.cavaleiros_texto):
            #click on group
            grup = self.driver.find_element_by_xpath(f"//span[@title='{self.grupos}']")
            time.sleep(0.5)
            grup.click()
            del grup
            #click on clip icon
            clip = self.driver.find_element_by_xpath("//span[@data-icon='clip']")
            time.sleep(2)
            clip.click()
            del clip
            #add file to send by file path
            localDafoto = self.driver.find_element_by_xpath("//input[@type='file']")
            time.sleep(1)
            localDafoto.send_keys(local)
            del localDafoto
            time.sleep(1)
            #send extra text
            caixa_texto = self.driver.find_element_by_class_name('_2S1VP')
            caixa_texto.click()
            caixa_texto.send_keys(texto)
            del caixa_texto
            #click to send
            envio = self.driver.find_element_by_xpath("//span[@data-icon='send-light']")
            time.sleep(1)
            envio.click()
            del envio
            self.hora = self.hora/4
            self.esperar_hora()
        sys.exit()

    def msgZero(self):
        #click on group
        grup = self.driver.find_element_by_xpath(f"//span[@title='{self.grupos}']")
        time.sleep(0.5)
        grup.click()
        #click on text
        caixa_texto = self.driver.find_element_by_class_name('_1Plpp')
        time.sleep(0.5)
        for msg in self.Zero_texto:
            caixa_texto.click()
            #write text
            caixa_texto.send_keys(msg)
            #send text
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(0.5)
            botao_enviar.click()
            time.sleep(random.randrange(1,10))

    def enviarMsg(self):
        #<span dir="auto" title="Comecou a dentadura" class="_1wjpf _3NFp9 _3FXB1">Comecou a dentadura</span>
        #<div tabindex="-1" class="_1Plpp">
        #<span data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        print('esperando muitos minutos')

        if self.tempo > 0:
            for msg in self.mensagem:
                if self.tempo>0:
                    self.driver.get('https://web.whatsapp.com/')
                    time.sleep(20)
                    #click on group
                    grup = self.driver.find_element_by_xpath(f"//span[@title='{self.grupos}']")
                    time.sleep(0.5)
                    grup.click()
                    del grup
                    #click on text
                    caixa_texto = self.driver.find_element_by_class_name('_1Plpp')
                    time.sleep(0.5)
                    caixa_texto.click()
                    #write text
                    caixa_texto.send_keys(msg)
                    del caixa_texto
                    #send text
                    botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(0.5)
                    botao_enviar.click()
                    del botao_enviar
            
                self.tempo= self.tempo-1
                print(self.tempo)

                #verificar se rafael ja colocou a foto
                for i in range(4):
                    self.driver.get('https://web.whatsapp.com/')
                    time.sleep(20)
                    time.sleep(self.hora/4)
                    self.verificarFto()

        #tempo zero
        if self.tempo==0:
            self.driver.get('https://web.whatsapp.com/')
            time.sleep(20)
            self.msgZero()
            self.tempo= self.tempo-1
            time.sleep(self.hora/4)

        #tempo negativo
        if self.tempo<0:
            self.driver.get('https://web.whatsapp.com/')
            time.sleep(20)
            self.FinalMsgs()
            self.tempo= self.tempo-1

bot = bot()
bot.FinalMsgs()