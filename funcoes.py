from doctest import ELLIPSIS_MARKER
import time
import datetime
import os
import random
from colorama import Fore 


def send_to_txt(msg, ponto=0):
    os.chdir(r"C:\\Users\\Public\\GERENCIADOR-SENHAS\\")
    log = open('log.txt', 'a')
    if ponto == 1:
        hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        log.write('\n')
        log.write('\n')
        log.write("*************************************************************************\n")
        log.write(f'{hora} -> {msg}\n')
        log.close()

    elif ponto == 2:
        hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        data = datetime.date.today()
        log.write(f'{hora} -> {msg}\n')
        log.close()

    else:
        hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
        data = datetime.date.today()
        log.write(f'{hora} -> {msg}\n')
        log.close()


def gerador_senhas(qtd):
    f = 0
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_grandes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    especiais = ['!', '@', '#', '$', '%', '*', '&']
    senha2 = []
    escolha = ['a','b','c','d']
    global confidencial
    while f < qtd:
        f += 1
        a = random.choice(especiais)
        b = random.randint(0, 9)
        c = random.choice(letras_grandes)
        d = random.choice(letras)
        decisao = random.choice(escolha)
                
        if decisao == 'a':
            senha2.append(a)    

        elif decisao == 'b':
            senha2.append(b)

        elif decisao == 'c':
            senha2.append(c)

        elif decisao == 'd':
            senha2.append(d)   

    random.shuffle(senha2)  
    print(Fore.GREEN + 'Senha gerada com sucesso!')
    senha = "".join(str(v) for v in senha2) 
    confidencial = senha


def decisao_de_senha():
    global confidencial
    while True:
        try:
            escolha = str(input("Deseja criar uma senha automática? ").lower())
            if escolha in 'simsyesy':
                qtd = int(input("Quantidade de caracteres: "))
                if qtd > 100:
                    print(Fore.YELLOW + 'Sua senha deve ter até 100 caractares!')
                    time.sleep(1)    
                    continue
                else: 
                    gerador_senhas(qtd)
                    time.sleep(1)
                    break
            else:
                confidencial = str(input("Senha: "))
                break
        except Exception as erro:
            print(erro)
            time.sleep(1)
            continue   
