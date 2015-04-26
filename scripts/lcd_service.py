__author__ = 'mliu'

import RPi.GPIO


def init_gpio():
    print 'Initializing GPIOs...'
    RPi.GPIO.setmode(RPi.GPIO.BCM)


def shutdown():
    print 'Shutting down...'
    return

print 'Starting Raspberry LCD Service...'
init_gpio()
shutdown()
print 'Good bye!'