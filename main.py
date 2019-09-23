import sys
print("NO ELO")
sys.stdout.flush()


import RPi.GPIO as GPIO
import time
import w1thermsensor

from datetime import datetime

LODOWKA = 3

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setup(LODOWKA, GPIO.OUT) # GPIO Assign mode

def log(a, on):
    now = datetime.now()
    t = now.strftime("%d/%m/%Y %H:%M:%S")
    print(str(t) + ": " + "temperature=" + temp + " on=" + on)
    sys.stdout.flush()
    try:
        file = open('./metrics.json', 'w')
        metrics = dict(time=str(t), temperature=a, on=)
        json.dump(metrics, file)



while True:
    sensor = w1thermsensor.W1ThermSensor()
    temp = sensor.get_temperature()

    if temp < 19:
        GPIO.output(lodowka, GPIO.LOW) # off
        log(temp, 0)
    elif temp > 21:
        GPIO.output(lodowka, GPIO.HIGH) # on
        log(temp, 1)
    else: 
    time.sleep(5)
