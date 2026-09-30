from time import sleep
from gpiozero import Device
from gpiozero.pins.mock import MockFactory
Device.pin_factory = MockFactory()
from gpiozero import LED, Buzzer, DistanceSensor

verde = LED(22)
amarillo = LED(27)
rojo = LED(17)
buzzer = Buzzer(4)

def leer_cm():
    return float(input("Distancia en cm (0 para salir): "))

while True:
    d = leer_cm()
    if d == 0:
        break
    verde.off(); amarillo.off(); rojo.off(); buzzer.off()
    if d > 50:
        verde.on()
    elif d > 20:
        amarillo.on(); buzzer.beep(0.2, 0.5, n=1)
    else:
        rojo.on(); buzzer.beep(0.1, 0.1, n=3)

    print(f"{d:.1f} cm -> verde:{verde.is_lit} amarillo:{amarillo.is_lit} rojo:{rojo.is_lit}")
    sleep(0.3)
