import RPi.GPIO as GPIO
import time

VERDE = 22
AMARILLO = 27
ROJO = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup([VERDE, AMARILLO, ROJO], GPIO.OUT)

try:
    while True:
        GPIO.output(VERDE, True)
        time.sleep(5)
        GPIO.output(VERDE, False)

        GPIO.output(AMARILLO, True)
        time.sleep(2)
        GPIO.output(AMARILLO, False)

        GPIO.output(ROJO, True)
        time.sleep(5)
        GPIO.output(ROJO, False)

except KeyboardInterrupt:
    print("Detenido")

finally:
    GPIO.cleanup()
