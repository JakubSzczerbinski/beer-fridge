import RPi.GPIO as GPIO
import time
import w1thermsensor
import sys
import json

from datetime import datetime

LODOWKA = 3

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setup(LODOWKA, GPIO.OUT) # GPIO Assign mode

def log(a, on):
    now = datetime.now()
    t = now.strftime("%d/%m/%Y %H:%M:%S")
    file = open('./metrics.json', 'w+')
    metrics = dict(time=str(t), temperature=a, on=on)
    json.dump(metrics, file)
    print(str(t) + ": " + "temperature=" + str(temp) + " on=" + str(on))
    sys.stdout.flush()
    

while True:
    sensor = w1thermsensor.W1ThermSensor()
    temp = sensor.get_temperature()

    if temp < 19:
        GPIO.output(LODOWKA, GPIO.LOW)

    if temp > 21:
        GPIO.output(LODOWKA, GPIO.HIGH)

    on = GPIO.input(LODOWKA)
    log(temp, on)

    time.sleep(5)

