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

Vamos usar a biblioteca [requests](https://requests.readthedocs.io/en/master/) para facilitar o nosso trabalho com as requisições HTTP, [argparse](https://docs.python.org/3/howto/argparse.html) para utilizarmos argumentos na linha de comando e [threading]() para usarmos vários threads que proporcionarão uma maior velocidade.

Caso não queira depender de bibliotecas, pode fazer todas as requisições na mão usando sockets.

### 