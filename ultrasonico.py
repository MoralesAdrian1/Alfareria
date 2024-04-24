from machine import Pin
import time

# Definimos los pines para el trigger y el echo del sensor ultrasónico
trig_pin = Pin(12, Pin.OUT)
echo_pin = Pin(14, Pin.IN)

# Definimos el pin para el relay
RELAY_PIN = 16
relay = Pin(RELAY_PIN, Pin.OUT)

def medir_distancia():
    # Enviamos un pulso de 10 microsegundos al pin de trigger
    trig_pin.on()
    time.sleep_us(10)
    trig_pin.off()
    
    # Esperamos a que el pin echo se ponga en alto
    while not echo_pin.value():
        pulse_start = time.ticks_us()
    
    # Esperamos a que el pin echo se ponga en bajo
    while echo_pin.value():
        pulse_end = time.ticks_us()
    
    # Calculamos la duración del pulso
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    
    # Convertimos la duración del pulso a distancia en centímetros
    distancia = (pulse_duration * 0.0343) / 2
    
    return distancia

while True:
    # Medimos la distancia
    distancia = medir_distancia()
    if distancia < 70:
        relay.value(0)  # Encender el relay
        time.sleep(1800)
    else:
        relay.value(1)  # Apagar el relay
    
    # Esperamos un segundo antes de tomar la siguiente medida
    time.sleep(1)
