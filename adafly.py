import serial,sys, threading, os
from Adafruit_IO import MQTTClient
def connected(client):
    print("Conectado com sucesso!")

def disconnected(client):
    print('Desconectado! :(')
    exit(1)

def message(client, topic_id, payload):
    print('Topico {0} : {1}'.format(topic_id, payload))

def inicia_cliente():
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    client.connect()
    client.loop_background()
    return client

def leitura_serial():
    try:
        with serial.Serial(PORTA,115200) as porta:
            client = inicia_cliente()
            while True:
                line = porta.readline().decode('UTF8').strip()
                print("Recebido: {}".format(line))
                prot = line.split('/')
                if len(prot) == 2:
                    client.publish(prot[0], prot[1], GRUPO)
                elif len(prot) == 3:
                    client.publish(prot[1], prot[2], prot[0])


    except Exception as ex:
        print("Erro durante a comunicação")
        print("--------------------------")
        print(ex)

        
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Favor informar todos parametros:\n python {} <porta> <usuario> <aio_key>".format(sys.argv[0]))
        exit()
    PORTA = sys.argv[1]
    ADAFRUIT_IO_USERNAME = sys.argv[2]
    ADAFRUIT_IO_KEY = sys.argv[3]
    GRUPO = os.getenv('ADAFLY_GROUP', 'microbit')
    thread = threading.Thread(target=leitura_serial)
    thread.start()
