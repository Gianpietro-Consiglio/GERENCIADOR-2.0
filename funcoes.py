import sqlite3
import time
import os
import random
from colorama import Fore 


def send_to_txt(msg):
    os.chdir(r"C:\\Users\\Public\\GERENCIADOR-SENHAS\\")
    log = open('log.txt', 'a')
    hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + 'Senha gerada com sucesso!')
    senha = "".join(str(v) for v in senha2) 
    confidencial = senha


def decisao_de_senha():
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_funcao = ("SIM", "NÃO")
    global confidencial
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("*" * 20)
        print("CRIAR SENHA ALEATÓRIA?")
        print("*" * 20)
        cont = 0
        for x in menu_funcao:
            cont += 1
            print(f'[{cont}]{x}')
        try:
            print('')
            escolha = int(input("Opção: "))
            if escolha == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                qtd = int(input("Quantidade de caracteres: "))
                if qtd > 100:
                    print(Fore.YELLOW + 'Sua senha deve ter até 100 caractares!')
                    time.sleep(1)    
                    continue
                else: 
                    gerador_senhas(qtd)
                    time.sleep(0.5)
                    break
            elif escolha == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                confidencial = str(input("Senha: "))
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

        except Exception as erro:
            send_to_txt(erro)
            continue   

def conexao():
    global query
    try:
        banco = sqlite3.connect('gerenciador.db')
        cursor = banco.cursor()
        cursor.execute('SELECT * FROM contas')
        query = cursor.fetchall()
        
    except:
        print('erro')    
