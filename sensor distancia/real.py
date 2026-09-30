import RPi.GPIO as GPIO
import time

# Pines (numeración BCM)
TRIG = 23
ECHO = 24
LED_VERDE = 22
LED_AMARILLO = 27
LED_ROJO = 17
BUZZER = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup([TRIG, LED_VERDE, LED_AMARILLO, LED_ROJO, BUZZER], GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(0.5)


def leer_cm():
    # Pulso de 10 microsegundos en Trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Esperar a que Echo suba
    limite = time.time() + 0.05
    inicio = time.time()
    while GPIO.input(ECHO) == 0:
        inicio = time.time()
        if inicio > limite:
            return 200.0

    # Esperar a que Echo baje
    fin = inicio
    while GPIO.input(ECHO) == 1:
        fin = time.time()
        if fin - inicio > 0.02:       # si pasa de 2 metros ignoramos
            return 200.0

    # distancia = velocidad del sonido x tiempo / 2
    cm = (fin - inicio) * 34300 / 2
    return min(cm, 200.0)


def apagar_todo():
    GPIO.output(LED_VERDE, False)
    GPIO.output(LED_AMARILLO, False)
    GPIO.output(LED_ROJO, False)
    GPIO.output(BUZZER, False)


def pitidos(veces, t_on, t_off):
    for _ in range(veces):
        GPIO.output(BUZZER, True)
        time.sleep(t_on)
        GPIO.output(BUZZER, False)
        time.sleep(t_off)


try:
    while True:
        d = leer_cm()
        apagar_todo()
        if d > 50:
            GPIO.output(LED_VERDE, True)
            zona = "VERDE"
        elif d > 20:
            GPIO.output(LED_AMARILLO, True)
            pitidos(1, 0.2, 0.1)
            zona = "AMARILLO"
        else:
            GPIO.output(LED_ROJO, True)
            pitidos(3, 0.1, 0.1)
            zona = "ROJO"

        print(f"{d:.1f} cm -> {zona}")
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Programa detenido")

finally:
    GPIO.cleanup()                    # libera los pines
