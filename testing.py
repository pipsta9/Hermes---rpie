import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'RED GPIO'
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)

'ORANGE GPIO'
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)

'BLUE GPIO'
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)

while True:
    'RED'
    input_state_red = GPIO.input(6)
    if input_state_red == False:
        print('Red Button Pressed')
        for x in range(8):
            GPIO.output(5, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(5, GPIO.HIGH)
            time.sleep(0.5)
        
    'ORANGE'
    input_state_orange = GPIO.input(24)
    if input_state_orange == False:
        print('Orange Button Pressed')
        for x in range(8):
            GPIO.output(23, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(23, GPIO.HIGH)
            time.sleep(0.5)
    'BLUE'
    input_state_blue = GPIO.input(21)
    if input_state_blue == False:
        print('Blue Button Pressed')
        for x in range(8):
            GPIO.output(20, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(20, GPIO.HIGH)
            time.sleep(0.5)
