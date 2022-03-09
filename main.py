#IMPORTAÇÕES
import sqlite3
import random
import time
import sys
import os
import emoji
import smtplib
import funcoes
from colorama import init, Fore 
from email.message import EmailMessage
#FIM
init(convert=True, autoreset=True)

#os.mkdir("C:\\Users\Public\\GERENCIADOR-SENHAS\\")
  

try:
    os.chdir("C:\\Users\Public\\GERENCIADOR-SENHAS\\")
except:
    pass    
try:
    banco = sqlite3.connect('gerenciador-senhas.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE user(id integer primary key, email text, nome text, senha text)")
    cursor.execute("CREATE TABLE contas(rlx integer primary key, identificador text, site text, usuario text, senha text)")
    banco.commit()
                     
except Exception as erro:
    funcoes.send_to_txt(erro)
    pass

print(Fore.YELLOW + "Aguarde...")
time.sleep(1)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    itens = ['Login', 'Cadastrar', 'Sobre', 'Sair']
    cont = 0
    for menu in itens:
        cont += 1
        print(f"[{cont}]{menu}")

    try:
        option = int(input("Opção -> "))

    except Exception as erro:
        funcoes.send_to_txt(erro)
        continue

    else:
        
        if option == 3:
            print(Fore.GREEN + "Banco de dados e log estão localizado no seguinte diretório: C:\\Users\Public\\GERENCIADOR-SENHAS\\ ")
            print(Fore.YELLOW + "Programa desenvolvido por Gianpietro Consiglio")
            print(Fore.BLUE + "Programa feito com a linguagem Python e Sqlite")
            saida = str(input("Aperte qualquer tecla para sair: "))

        elif option == 1:
            #os.chdir("C:\\Users\Public\\GERENCIADOR-SENHAS\\")
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
                login_valid = cursor.fetchall()
                senha_valid = cursor2.fetchall()
                for x in login_valid:
                    c = x
                for b in c:
                    d = b
                for x in senha_valid:
                    e = x
                for f in e:
                    g = f

            except Exception as erro:
                funcoes.send_to_txt(erro)
                print(Fore.RED + "Erro ao logar!")
                time.sleep(1)
                banco.close()
                continue

            os.system('cls' if os.name == 'nt' else 'clear')

            if login == d and senha == g:
                print(Fore.GREEN + "Login realizado com sucesso!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            else:
                print(Fore.RED + "Credenciais inválidas!")
                time.sleep(1)
                banco.close()
                continue
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.BLUE + f"Bem-Vindo, {login}".upper())
            time.sleep(1)
            
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.BLUE + f"Conta -> {login}")
                menu = ["Cadastrar Credencial", "Ver Credenciais","Alterar Credenciais", "Excluir Credencial","Excluir conta","Sair"]
                cont = 0
                for x in menu:
                    cont +=1
                    print(f"[{cont}]{x}")
                try:
                    option = int(input("Opção -> "))

                except:
                    continue

                else:
                    if option == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        site = str(input("Site: "))
                        nick = str(input("Usuário: "))
                        funcoes.decisao_de_senha()

                        try:
                            cursor.execute("INSERT INTO contas(identificador, site, usuario, senha) VALUES('"+ login +"', '"+ site +"', '" + nick + "', '" + funcoes.confidencial + "')")
                            banco.commit()
                            
                        except Exception as erro:
                            funcoes.send_to_txt(erro)
                            print(Fore.RED + "Erro ao enviar dados")  
                            banco.close()
                            time.sleep(1)
                            continue  
                        else:
                            print(Fore.GREEN + "Dados enviados com sucesso")
                            time.sleep(1)
                            continue

                    elif option == 2:
                        a = ''
                        try:
                            x = cursor.execute(f"SELECT site, usuario, senha FROM contas WHERE identificador = '{login}'")
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
                            for a in x:
                                print(a)
                            print('')    
                            exit = str(input("Aperte quaquer tecla para sair: "))
                            continue

                    elif option == 3:
                        cont = 0
                        try:
                            x = cursor.execute(f"SELECT rlx, site, usuario, senha FROM contas WHERE identificador = '{login}'")
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
                            option = int(input("Opção -> ")) 
                            option = option - 1
                            alvo = list(x[option])
                            for b in alvo:
                                alvo1.append(b) 
                            user = str(input("Novo usuário: "))    
                            funcoes.decisao_de_senha()
              
                            try:
                                cursor.execute(f"UPDATE contas SET usuario = '{user}' WHERE rlx = {alvo1[0]}")  
                                cursor.execute(f"UPDATE contas SET senha = '{funcoes.confidencial}' WHERE rlx = {alvo[0]}")
                                banco.commit()

                            except Exception as erro:
                                funcoes.send_to_txt(erro)   
                                print(Fore.RED + "Erro ao alterar nova credencial!")  
                                time.sleep(1)

                            else:
                                print(Fore.GREEN + "Credencial alterada!") 
                                time.sleep(1)    
                            

                    elif option == 4:
                        cont = 0
                        try:
                            x = cursor.execute(f"SELECT rlx, site, usuario, senha FROM contas WHERE identificador = '{login}'")
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
                            option = int(input("Opção -> ")) 
                            option = option - 1
                            alvo = list(x[option])
                            for b in alvo:
                                alvo1.append(b)  
                            try:
                                cursor.execute(f"DELETE FROM contas WHERE rlx = {alvo1[0]}")   

                            except Exception as erro:
                                funcoes.send_to_txt(erro)  
                                print(Fore.RED + "Erro ao excluir credencial!") 
                                time.sleep(1)

                            else:
                                print(Fore.GREEN + "Credencial excluída!")
                                time.sleep(1)
                        

                    elif option == 5:
                        try:
                            cursor.execute(f"DELETE FROM contas WHERE identificador = '{login}'")
                            cursor.execute(f"DELETE FROM user WHERE nome = '{login}'")
                            banco.commit()

                        except Exception as erro:
                            funcoes.send_to_txt(erro)
                            print(Fore.RED + "Erro ao excluir sua conta!") 
                            time.sleep(1)   
                        else:
                            print(Fore.GREEN + "Conta excluída!")
                            time.sleep(1)
                            sys.exit()

                    else:
                        break     



                         

        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear')     
            
            nome = str(input("Nome: ").lower())
            try:
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

                meu_email = 'gianpietro.consiglio1807@gmail.com'   
                minha_senha = 'IP-37UYQ067'  
                msg = EmailMessage()
                msg['Subject'] = f'Código = {str(chave)[1:-1]}'
                msg['From'] = meu_email  #adicionado para linux
                msg['To'] = email
                msg.add_alternative(
                        """
                        <!DOCTYPE HTML>
                        <html>
                        <body style="text-transform: uppercase; background-color: black; width: 800px; height: 600px; color: white; margin: auto;">
                        <h1 style="text-align: center">e-mail automático do programa gerenciador de senhas</h1>
                        <p style="text-align: center;">não responder esse e-mail</p>
                        <p style="text-align: center;">copiar código acima e colar no programa que está sendo executado</p>
                        <p style="text-align: center; color: red;>por gentileza, copiar todo o código após 'código =' que se econtra na parte de assunto do e-mail</p>
                        <p style="text-align: center; font-size: 12px;">programa desenvolvido por Gianpietro Consiglio</p>
                        </body>
                        </html>
                        """, subtype = "html")
                chave_transform = str(chave)[1:-1]

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
                        print(Fore.GREEN + f"MENSAGEM ENVIADA COM SUCESSO!{emoji.emojize(':thumbsup:', use_aliases=True)}")  
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        resposta_email = str(input("Verificar código: "))


            
            os.system('cls' if os.name == 'nt' else 'clear')
            if resposta_email == chave_transform:
                print(Fore.GREEN + "E-mail verificado com sucesso!")
                time.sleep(1)

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
                cursor.execute("INSERT INTO user(email, nome, senha) VALUES('"+ email +"','" + nome + "', '" + senha + "')")
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
                        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + 'Saindo...')
            time.sleep(1)
            break    
        