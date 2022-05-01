#IMPORTAÇÕES
import sqlite3
import random
import time
import sys
import os
import smtplib
import pyperclip
import funcoes
import webbrowser as wb
from colorama import init, Fore 
from email.message import EmailMessage
#FIM
init(convert=True, autoreset=True)

try:
    os.mkdir(r"C:\\Users\\Public\\GERENCIADOR-SENHAS\\")
except:
    pass 

try:
    os.chdir("C:\\Users\Public\\GERENCIADOR-SENHAS\\")
except:
    pass   

try:
    banco = sqlite3.connect('gerenciador-senhas.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE user(id integer primary key, email text, nome text, senha text, cadastro text, ultima_alteracao text)")
    cursor.execute("CREATE TABLE contas(id integer primary key, nome text, site text, usuario text, senha text, cadastro text, ultima_alteracao text)")
    banco.commit()
                     
except Exception as erro:
    funcoes.send_to_txt(erro)
    pass

print(Fore.YELLOW + "Aguarde...")
time.sleep(0.5)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    itens = ['Login', 'Cadastrar', 'Sobre', 'Sair']
    cont = 0
    for menu in itens:
        cont += 1
        print(f"[{cont}]{menu}")

    try:
        escolha = int(input("Opção -> "))

    except Exception as erro:
        funcoes.send_to_txt(erro)
        continue

    else:
        # TRECHO REALIZAÇÃO DE LOGIN
        if escolha == 1:
            try:
                banco = sqlite3.connect("gerenciador-senhas.db")
                cursor = banco.cursor()
                cursor2 = banco.cursor()
                os.system('cls' if os.name == 'nt' else 'clear')
                login = str(input("Nome: ").lower())
                senha = str(input("Senha: "))
                cursor.execute("SELECT nome FROM user WHERE nome = '" + login + "'")
                cursor2.execute("SELECT senha FROM user WHERE nome = '" + login + "' ")
                banco.commit()
                compara_login = cursor.fetchall()
                compara_senha = cursor2.fetchall()
                
                compara_login_transform = str(compara_login)
                compara_login_transform = compara_login_transform.replace("(", "").replace(")", "").replace("[","").replace("]","").replace(",","").replace("'","")
                compara_senha_transform = str(compara_senha)
                compara_senha_transform = compara_senha_transform.replace("(", "").replace(")", "").replace("[","").replace("]","").replace(",","").replace("'","")
           
            except Exception as erro:
                funcoes.send_to_txt(erro)
                print(Fore.RED + "Não foi possível verificar login!")
                time.sleep(1)
                banco.close()
                continue

            
            
            if login == compara_login_transform and senha == compara_senha_transform:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Login realizado com sucesso!")
                time.sleep(0.5)

                                                
            else:
                print(Fore.RED + "Login ou senha não correspondem!")
                time.sleep(1)
                banco.close()
                continue

        # TRECHO REALIZAÇÃO DE CADASTRO
        elif escolha == 2:
            os.system('cls' if os.name == 'nt' else 'clear')     
            
            nome = str(input("Nome: ").lower())
            try:
                banco = sqlite3.connect('gerenciador-senhas.db')
                cursor = banco.cursor()
                cursor.execute("SELECT nome FROM user WHERE nome = '" + nome + "' ")
                banco.commit()

            except Exception as erro:
                funcoes.send_to_txt(erro) 
                print(Fore.RED + "Erro ao fazer verificação da disponiblidade de nome")
                time.sleep(1)   
                continue

            validar = cursor.fetchall()
            lista = list(validar)
            if len(lista) != 0:
                print(Fore.YELLOW + "Nome já utilizado!")
                time.sleep(1)
                banco.close()
                continue
                                   
            else:
                senha = str(input("Senha: "))
                email = str(input("E-mail: "))
                print(Fore.YELLOW + "Enviando e-mail...")
                c = 0
                chave = []
                while c < 6:
                    c+=1
                    num = random.randint(0,9)
                    chave.append(num)
                codigo = str(chave)
                codigo = codigo.replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace(" ", "")    
                
                """ E-MAIL CRIADO PARA FINS DE TESTES """
                meu_email = 'testegerenciadorpython@gmail.com'   
                minha_senha = 'batatapreta29'  
                msg = EmailMessage()
                msg['Subject'] = 'Verificação de conta'
                msg['To'] = email
                msg.add_alternative(
                        F"""
                        <!DOCTYPE HTML>
                        <html>
                        <body style="text-transform: uppercase; background-color: black; width: 800px; height: 600px; color: white; margin: auto;">
                        <h1 style="text-align: center">e-mail automático do programa gerenciador de senhas</h1>
                        <h2 style="text-align: center;">SEU CÓDIGO - {codigo} </h2>
                        <p style="text-align: center;">copiar código acima e colar no programa que está sendo executado</p>
                        </body>
                        </html>
                        """, subtype = "html")
                
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    try:
                        smtp.login(meu_email, minha_senha)
                        
                        
                    except Exception as erro:
                        print(Fore.RED + "Erro ao logar!")
                        funcoes.send_to_txt(erro)
                        time.sleep(1)
                        continue

                    try:
                        smtp.send_message(msg)

                    except Exception as erro:
                        print(Fore.RED + "Erro ao enviar e-mail!")
                        funcoes.send_to_txt(erro)
                        time.sleep(1)
                        continue

                    else:
                        print(Fore.GREEN + 'MENSAGEM ENVIADA!')
                        time.sleep(0.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        resposta_email = str(input("Verificar código: "))


            
            os.system('cls' if os.name == 'nt' else 'clear')
            if resposta_email == codigo:
                print(Fore.GREEN + "E-mail verificado com sucesso!")
                time.sleep(0.5)

            else:
                try:
                    # a ideia de passar a função sem argumento algum é proposital, assim forçando o erro e indo para o except
                    funcoes.send_to_txt()
                    
                except Exception as erro:
                    print(Fore.RED + "Não foi possível verificar seu e-mail!")
                    funcoes.send_to_txt(erro)
                    time.sleep(1)
                    continue
                
                           
            try:
                hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
                cursor.execute("INSERT INTO user(email, nome, senha, cadastro) VALUES('"+ email +"','" + nome + "', '" + senha + "', '"+ hora +"')")
                banco.commit()
                                
            except Exception as erro:
                print(Fore.RED + "Falha ao enviar seus dados!")
                funcoes.send_to_txt(erro)
                banco.close()
                continue

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Sucesso ao enviar seus dados!")
                time.sleep(1)  

        # TRECHO REALIZAÇÃO DE AJUDA
        elif escolha == 3:
            print(Fore.GREEN + "Banco de dados e log estão localizado no seguinte diretório: C:\\Users\Public\\GERENCIADOR-SENHAS\\ ")
            print(Fore.YELLOW + "Programa desenvolvido por Gianpietro Consiglio")
            print(Fore.BLUE + "Programa feito com a linguagem Python e Sqlite")
            saida = str(input("Aperte qualquer tecla para sair: "))
                        
        # TRECHO REALIZAÇÃO DE SAÍDA                
        elif escolha == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + 'Saindo...')
            time.sleep(1)
            break  

        else:
            continue




        # TRECHO REALIZAÇÃO DE FUNÇÕES QUANDO JÁ LOGADO
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print(Fore.WHITE + f"Bem-Vindo, {login}".upper())
            time.sleep(0.5)

        except Exception as erro:
            print("Erro ao carregar seu espaço privado!")
            funcoes.send_to_txt(erro)    
            continue

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.WHITE + f"Conta -> {login}")
            menu = ["Cadastrar Credencial", "Ver Credenciais","Alterar Credenciais", "Excluir Credencial","Excluir conta","Alterar detalhes da conta","Sair"]
            cont = 0
            for x in menu:
                cont +=1
                print(f"[{cont}]{x}")
            try:
                escolha = int(input("Opção: "))
                os.system('cls' if os.name == 'nt' else 'clear')

            except:
                continue

            else:
                # TRECHO LOGADO - CADASTRAR CREDENCIAL
                if escolha == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    site = str(input("Site: "))
                    nick = str(input("Usuário: "))
                    funcoes.decisao_de_senha()
                    try:
                        hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
                        cursor.execute("INSERT INTO contas(nome, site, usuario, senha, cadastro) VALUES('"+ login +"', '"+ site +"', '" + nick + "', '" + funcoes.confidencial + "', '"+ hora +"')")
                        banco.commit()
                            
                    except Exception as erro:
                        funcoes.send_to_txt(erro)
                        print(Fore.RED + "Erro ao enviar dados")  
                        banco.close()
                        time.sleep(1)
                        continue  
                    else:
                        print(Fore.GREEN + "Dados enviados com sucesso")
                        time.sleep(0.5)
                        continue
                # TRECHO LOGADO - VER CREDENCIAIS CADASTRADAS 
                elif escolha == 2:
                    a = ''
                    try:
                        x = cursor.execute(f"SELECT site, usuario, senha FROM contas WHERE nome = '{login}'")
                        banco.commit()
                        x = cursor.fetchall()
                                                                           
                    except Exception as erro:
                        funcoes.send_to_txt(erro)   
                        print(Fore.RED + "Falha na pesquina de informações")  
                        time.sleep(2)
                        continue

                    else:
                        if len(x) == 0:
                            print(Fore.RED + "Sem credenciais cadastradas!")
                            time.sleep(1)
                            continue
                        else:
                            c = 0
                            for a in x:
                                c+=1
                                print(f'[{c}]{a}')
                            try:
                                escolha = int(input("Opção: "))

                            except Exception as erro:
                                funcoes.send_to_txt(erro)
                                continue
                            if escolha > c:
                                continue

                            os.system('cls' if os.name == 'nt' else 'clear')

                            # TRECHO LADO - SUB MENU - ACCS    
                            while True:
                                options = 0
                                os.system('cls' if os.name == 'nt' else 'clear')
                                menu = ['ABRIR SITE','COPIAR LOGIN', 'COPIAR SENHA', 'SAIR']
                                for x in menu:
                                    options += 1
                                    print(f'[{options}]{x}')

                                try:
                                    options = int(input('Opção: '))

                                except Exception as erro:
                                    funcoes.send_to_txt(erro)
                                    continue    

                                if options == 1:
                                    x = cursor.execute(f"SELECT site FROM contas WHERE nome = '{login}' AND id = {escolha}")
                                    banco.commit()
                                    x = cursor.fetchall() 
                                    site = str(x)
                                    site = site.replace("(","").replace(")","").replace("[","").replace("]","").replace("'","").replace(",","")
                                    wb.open(site)
                                    
                                elif options == 2:
                                    x = cursor.execute(f"SELECT usuario FROM contas WHERE nome = '{login}' AND id = {escolha} ")
                                    banco.commit()
                                    x = cursor.fetchall()
                                    usuario = str(x)
                                    usuario = usuario.replace("(","").replace(")","").replace("[","").replace("]","").replace("'","").replace(",","")   
                                    pyperclip.copy(usuario)  
                                    print(Fore.GREEN + 'Usuário copiado para área de transferência!')
                                    time.sleep(1)

                                elif options == 3:
                                    x = cursor.execute(f"SELECT senha FROM contas WHERE nome = '{login}' AND id = {escolha} ")
                                    banco.commit()
                                    x = cursor.fetchall()
                                    senha = str(x)
                                    senha = senha.replace("(","").replace(")","").replace("[","").replace("]","").replace("'","").replace(",","")   
                                    pyperclip.copy(senha)  
                                    print(Fore.GREEN + 'Senha copiada para área de transferência!')
                                    time.sleep(1)

                                else:
                                    break    

                                
                                    


                # TRCHO LOGADO - ALTERAR CREDENCIAIS
                elif escolha == 3:
                    cont = 0
                    try:
                        x = cursor.execute(f"SELECT id, site, usuario, senha FROM contas WHERE nome = '{login}'")
                        banco.commit()
                        x = cursor.fetchall()

                    except Exception as erro:
                        funcoes.send_to_txt(erro)   
                        print(Fore.RED + "Falha na pesquina de informações")  
                        continue

                    else:
                        if len(x) == 0:
                            print(Fore.RED + "Sem credenciais cadastradas!")
                            time.sleep(1)
                            continue
                        alvo1 = []
                        for a in x:
                            cont += 1
                            print(f"[{cont}]{a}")
                        escolha = int(input("Opção -> ")) 
                        escolha = escolha - 1
                        alvo = list(x[escolha])
                        for b in alvo:
                            alvo1.append(b) 
                        user = str(input("Novo usuário: "))    
                        funcoes.decisao_de_senha()
              
                        try:
                            hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
                            cursor.execute(f"UPDATE contas SET usuario = '{user}' WHERE id = {alvo1[0]}")  
                            cursor.execute(f"UPDATE contas SET senha = '{funcoes.confidencial}' WHERE id = {alvo[0]}")
                            cursor.execute(f"UPDATE contas SET ultima_alteracao = '{hora}'")
                            banco.commit()

                        except Exception as erro:
                            funcoes.send_to_txt(erro)   
                            print(Fore.RED + "Erro ao alterar nova credencial!")  
                            time.sleep(1)

                        else:
                            print(Fore.GREEN + "Credencial alterada!") 
                            time.sleep(0.5)    
                            
                # TRECHO LOGADO - DELETAR CREDENCIAIS
                elif escolha == 4:
                    cont = 0
                    try:
                        x = cursor.execute(f"SELECT site, usuario, senha FROM contas WHERE nome = '{login}'")
                        z = cursor2.execute(f"SELECT id FROM contas WHERE nome = '{login}'")
                        banco.commit()
                        x = cursor.fetchall()
                        z = cursor2.fetchall()

                    except Exception as erro:
                        funcoes.send_to_txt(erro)   
                        print(Fore.RED + "Falha na pesquina de informações")  
                        continue

                    else:
                        if len(x) == 0:
                            print(Fore.RED + "Sem credenciais cadastradas!")
                            time.sleep(0.5)
                            continue
                        alvo1 = []
                        for a in x:
                            cont += 1
                            print(f"[{cont}]{a}")
                        try:
                            escolha = int(input("Opção: ")) 
                            if escolha > cont:
                                continue
                            else:
                                pass

                        except Exception as erro:
                            funcoes.send_to_txt(erro)
                            continue

                        else:
                            escolha = escolha - 1
                        alvo = list(z[escolha])
                        
                        for b in alvo:
                            alvo1.append(b)  
                        
                        try:
                            cursor.execute(f"DELETE FROM contas WHERE id = {alvo1[0]}")   

                        except Exception as erro:
                            funcoes.send_to_txt(erro) 
                            print(Fore.RED + "Erro ao excluir credencial!") 
                            time.sleep(1)

                        else:
                            print(Fore.GREEN + "Credencial excluída!")
                            time.sleep(0.5)
                        
                # TRECHO LOGADO - EXCLUIR CONTA 
                elif escolha == 5:
                    try:
                        cursor.execute(f"DELETE FROM contas WHERE nome = '{login}'")
                        cursor.execute(f"DELETE FROM user WHERE nome = '{login}'")
                        banco.commit()

                    except Exception as erro:
                        funcoes.send_to_txt(erro)
                        print(Fore.RED + "Erro ao excluir sua conta!") 
                        time.sleep(1)   
                    else:
                        print(Fore.GREEN + "Conta excluída!")
                        time.sleep(0.5)
                        sys.exit()
                    
                # TRECHO LOGADO - ALTERAR DADOS DE CONTA PESSOAL CADASTRADA
                elif escolha == 6:
                    os.system('cls' if os.name == 'nt' else 'clear')     
                    cont = 0
                    menu = ['E-MAIL', 'NOME', 'SENHA']
                    for x in menu:
                        cont += 1
                        print(f"[{cont}]{x}")
                    try:
                        option = int(input("O que deseja alterar? "))  

                    except Exception as erro:
                        funcoes.send_to_txt(erro)
                        continue    

                    if option == 1:
                        email = str(input("Novo e-mail: ")) 
                        try:
                            hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
                            cursor.execute(f"UPDATE user SET email = '{email}' WHERE nome = '{login}' ")
                            cursor.execute(f"UPDATE user SET ultima_alteracao = '{hora}'")
                            banco.commit()

                        except Exception as erro:
                            funcoes.send_to_txt(erro)
                            print(Fore.RED + "Erro ao enviar informações") 
                            time.sleep(1)

                        else:
                            print(Fore.GREEN + "E-mail alterado com sucesso!")  
                            time.sleep(1)  

                    elif option == 2:
                        nome = str(input("Novo nome: "))  
                        try:
                            hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
                            cursor.execute(f"UPDATE user SET nome = '{nome}' WHERE nome = '{login}' ")
                            cursor.execute(f"UPDATE contas SET nome = '{nome}' WHERE nome = '{login}' ")
                            cursor.execute(f"UPDATE user SET ultima_alteracao = '{hora}'")
                            banco.commit()

                        except Exception as erro:
                            funcoes.send_to_txt(erro)
                            print(Fore.RED + "Erro ao enviar informações") 
                            time.sleep(1)

                        else:
                            print(Fore.GREEN + "Nome alterado com sucesso!")  
                            time.sleep(0.5)  
                            sys.exit() 

                    elif option == 3:
                        senha = str(input("Nova senha: "))
                        try:
                            cursor.execute(f"UPDATE user SET senha = '{senha}' WHERE nome = '{login}' ")
                            cursor.execute(f"UPDATE user SET ultima_alteracao = '{hora}'")
                            banco.commit()

                        except Exception as erro:
                            funcoes.send_to_txt(erro)
                            print(Fore.RED + "Erro ao enviar informações") 
                            time.sleep(1)

                        else:
                            print(Fore.GREEN + "Senha alterada com sucesso!")  
                            time.sleep(0.5)   
                            sys.exit()
                    
                # TRECHO LOGADO - SAIR
                elif escolha == 7:
                    break

                else:
                    continue
                   