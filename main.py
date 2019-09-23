import sys
print("NO ELO")
sys.stdout.flush()


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
lodowka = 3
GPIO.setup(lodowka, GPIO.OUT) # GPIO Assign mode


def log(a):
    from datetime import datetime
    now = datetime.now()
    t = now.strftime("%d/%m/%Y %H:%M:%S")
    print(str(t) + ": " + str(a))
    sys.stdout.flush()


while True:
    import time
    import w1thermsensor
    sensor = w1thermsensor.W1ThermSensor()
    temp = sensor.get_temperature()
    log(temp)

    if temp < 19:
        GPIO.output(lodowka, GPIO.LOW) # off
        log("turned off")
    elif temp > 21:
        GPIO.output(lodowka, GPIO.HIGH) # on
        log("turned on")
    else: 
        log("not changing state")
    time.sleep(5)
