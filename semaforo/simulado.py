from gpiozero import Device, LED
from gpiozero.pins.mock import MockFactory
from time import sleep

Device.pin_factory = MockFactory()

verde = LED(22)
amarillo = LED(27)
rojo = LED(17)

while True:
    verde.on()
    print("VERDE encendido:", verde.is_lit)
    sleep(5)
    verde.off()

    amarillo.on()
    print("AMARILLO encendido:", amarillo.is_lit)
    sleep(2)
    amarillo.off()

    rojo.on()
    print("ROJO encendido:", rojo.is_lit)
    sleep(5)
    rojo.off()
