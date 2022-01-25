import machine
import time

led = machine.Pin(13)

state = False
while True:
    time.sleep(1)
    led.on() if state else led.off()
    state = not state
