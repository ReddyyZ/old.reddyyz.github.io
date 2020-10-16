---
layout: post
title:  "Permissões no Linux"
date:   2020-10-09 20:00:00 -0300
categories: linux
author: "ReddyyZ"
lang: pt-BR
tags: [linux, file permissions]
reading_time: 2 minutes
description: Nesse artigo você irá aprender como funcionam as permissões dos arquivos no Linux, como usar o chmod e administrar o seu servidor Linux.
image: https://reddyyz.github.io/assets/images/permissions-codes.png
---

Nesse artigo você irá aprender como funcionam as permissões dos arquivos no Linux, como usar o chmod e administrar o seu servidor Linux.

### Como funcionam as permissões no Linux

```sh
┌─[reddyyz@parrot]─[~]
└──╼ $ls -la test.txt
-rw-r--r-- 1 reddyyz reddyyz 0 out  9 19:24 test.txt
```
> Permissões: `-rw-r--r--`

As permissões do arquivo são divididas em 3 partes:

```sh
-rw-  r--  r--
 |     |    |
 |     |   Outros
 |     |
 |    Grupo
 Dono
```

A primeira parte se refere as permissões do dono do arquivo, a segunda ao grupo dono do arquivo, e a terceira aos outros usuários.

Existem 3 permissões básicas:

```
R = Read    - Ler
W = Write   - Escrever
X = Execute - Executar
```

### Definindo as permissões de um arquivo

No Linux, as permissões são definidas em "códigos", que usaremos para definir as permissões de um arquivo usando a ferramenta `chmod`.

![Permissions Codes](/assets/images/permissions-codes.png)

```
7 - Todas as permissões
6 - Leitura e escrita
5 - Leitura e execução
4 - Leitura
3 - Escrita e execução
2 - Escrita
1 - Execução
0 - Nenhuma permissão
```

Vamos re-definir as permissões do arquivo `test.txt` para estas permissões:

```
Dono   - Leitura e escrita
Grupo  - Leitura e escrita
Outros - Nenhuma permissão
```

Agora vamos modificar as permissões do arquivo:

```sh
chmod 660 test.txt
```
<button class="copy" onClick="copy_to_clip2('chmod 660 test.txt')">Copiar comando</button>


Executando o comando e lendo novamente as permissões do arquivo temos o seguinte resultado:

```
┌─[reddyyz@parrot]─[~]
└──╼ $chmod 660 test.txt
┌─[reddyyz@parrot]─[~]
└──╼ $ls -la test.txt
-rw-rw---- 1 reddyyz reddyyz 0 out  9 19:24 test.txt
```

### Obrigado!

Obrigado por ler até aqui! Caso tenha alguma dúvida entre no meu servidor do discord e pergunte!<br>
[Discord Server](https://discord.gg/v5d3PZ9)
<br>