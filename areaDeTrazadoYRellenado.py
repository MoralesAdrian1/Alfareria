# Importa las clases y funciones necesarias desde los módulos correspondientes
from machine import Pin
from time import sleep
import network
from umqtt.simple import MQTTClient

# Definición de pines para los relés
RELAY_PIN = 22
RELAY_PIN2 = 15

# Configura los pines de los relés como salidas
relay = Pin(RELAY_PIN, Pin.OUT)
relay2 = Pin(RELAY_PIN2, Pin.OUT)

# Configuración de parámetros para la conexión MQTT
MQTT_BROKER = "192.168.157.135"  # Dirección IP del servidor MQTT
MQTT_USER = ""                    # Usuario MQTT (si es necesario)
MQTT_PASSWORD = ""                # Contraseña MQTT (si es necesaria)
MQTT_CLIENT_ID = ""               # ID de cliente MQTT
MQTT_TOPIC = "utng/AMOR/bodega2" # Tópico al que se suscribirá el cliente MQTT
MQTT_PORT = 1883                  # Puerto MQTT

# Función que se ejecuta cuando llega un mensaje MQTT
def llegada_mensaje(topico, msg):
    print(msg)  # Imprime el mensaje recibido
    # Controla los relés en función del mensaje recibido
    if msg == b'2':
        relay.value(0)  # Activa el relé 1
    if msg == b'3':
        relay.value(1)  # Desactiva el relé 1
    if msg == b'6':
        relay2.value(0) # Activa el relé 2
    if msg == b'7':
        relay2.value(1) # Desactiva el relé 2

# Función para suscribirse al servicio MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER,
        port=MQTT_PORT,
        user=MQTT_USER,
        password=MQTT_PASSWORD,
        keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado en %s, al topico %s"%(MQTT_BROKER, MQTT_TOPIC))
    return client

# Función para conectar el dispositivo a la red WiFi
def conectar_wifi():
    print("Conectando a WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Adrian', '123456ad')  # Nombre de la red y contraseña
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.1)
    print("  Conectado!  ")

# Conexión a la red WiFi y suscripción al servicio MQTT
conectar_wifi()  # Conecta a la red WiFi
client = subscribir()  # Suscribe al cliente al servicio MQTT

# Bucle principal para esperar y procesar los mensajes MQTT
while True:
    client.wait_msg()  # Espera y procesa los mensajes MQTT
