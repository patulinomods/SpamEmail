import os
import sys
import time
import smtplib
import colorama
import ctypes
from colorama import Fore

ctypes.windll.kernel32.SetConsoleTitleW('-SPAM DE EMAIL BY PATOMAKER-')
if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(f'''{Fore.RESET}


    Criador: PatoMaker
    
   [{Fore.RED}!{Fore.RESET}] Opa, aki vai um rapido tutorial de como usar , crie um gmail com a senha 123456789Aa., assim q criou va nesse site( logado com a conta criada) e abilite a opçao -> https://myaccount.google.com/lesssecureapps, assim q voce fez isso e so imformar o seu email criado, e a senha( obs: esse email sera utilizado para dar o spam).
    '''+Fore.RESET)

print('')
print('')

spamemail = input(f" [{Fore.RED}?{Fore.RESET}] Imforme seu email criado de acordo com o tuto: ")
spampassword = input(f" [{Fore.RED}?{Fore.RESET}] Imforme sua senha criada de acordo com o tuto: ")

email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

try:
    email.login(spamemail, spampassword)
except smtplib.SMTPAuthenticationError:
    print("")
    print(f" [{Fore.RED}!{Fore.RESET}] {Fore.RED}Email ou senha incorretas")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.RED}Ou voce nao seguiu o tutorial e ativou a opçao do site ao lado (https://myaccount.google.com/lesssecureapps)")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] Saindo em 5 segundos")
    time.sleep(5)
    exit()

print("")
print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN}Gmail e senha corretos..")
print("")
victimemail = input(f"{Fore.RESET} [{Fore.RED}?{Fore.RESET}]Qual Email Da Vitima?: ")
message = input(f" [{Fore.RED}?{Fore.RESET}] Qual Mensagem deseja emviar?: ")
number = int(input(f" [{Fore.RED}?{Fore.RESET}] Quantas vezes?: "))

print("")
print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN} Ok, Jaja irei começar o atake!{Fore.RESET}")
print("")

try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(spamemail,spampassword)
    i = 0
    print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN} iniciando o atake... \n{Fore.RESET}")
    print('')
    while i < number:
        i+=1
        server.sendmail(spamemail,victimemail,message)
        if i == 1:
            print((f' [{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado! 卍 ')%(i))
        elif i == 2:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 3:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 4:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 5:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 6:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 7:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 8:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 9:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        elif i == 0:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email enviado!  ')%(i))
        else:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}'' [%d] Email enviado!  ')%(i))
        sys.stdout.flush()
    print("")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN} O e-mail foi colocado em uma base de dados")
    print('')
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] Fexando em 3 segundos...")
    time.sleep(3)
    exit()

except KeyboardInterrupt:
    print("")
    print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN} O e-mail não foi colocado em uma base de dados")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}]fexando em 3 segundos...")
    time.sleep(3)
    exit()
