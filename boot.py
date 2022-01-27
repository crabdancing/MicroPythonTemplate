import machine
import time

# And example of writing a library
from lib.hello_world import hello_world

hello_world()

led = machine.Pin(13)

state = False
while True:
    print('LED state: ' + str(state))
    led.on() if state else led.off()
    state = not state
    time.sleep(1)
