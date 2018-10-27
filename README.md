# adafly

adafly é um script escrito em python que faz a ponte entre o dispositivo conectado na serial (microbit, arduino, nodemcu, etc..) e a plataforma Adafruit.IO.

## Requisitos

Python 3.4+
Dependências no arquivo `requirements.txt`, apenas rode `pip -r requirements.txt`.

## Getting Started

Executar o script com os seguintes argumentos:
`python adafly.py <porta> <adafruit_user> <aio_key>`


|||
|--------|----------------------------|
| `porta` | Porta serial utilizada, ex.: 'COM10' |
|`adafruit_user`| Usuário criado na plataforma Adafruit.IO|
| `aio_key` | AIO key, gerada na plataforma Adafruit.IO|

> Configuração de comunicação 115200, 8 bits, sem paridade, 1 stopbit

Após o microcontrolador pode enviar mensagem, utilizando:
`<grupo>/<feed>/<valor>`, ex.: `microbit/temperatura/22.5`
ou setando um grupo padrão pela variável de ambiente `ADAFLY_GROUP`, podendo mandar a mensagem utilizando:
`<feed>/<valor>`


  