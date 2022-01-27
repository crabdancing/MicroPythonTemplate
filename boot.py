import machine
import time
import typing

# And example of writing a library
from lib.hello_world import hello_world

hello_world()

led = machine.Pin(13)

state = False
for i in range(3):
    print('LED state: ' + str(state))
    led.on() if state else led.off()
    state = not state
    time.sleep(1)
