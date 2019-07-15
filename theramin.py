from time import sleep
from ptprotoplus import sensors, psonic
from gpiozero import Button

button = Button(26)
while True:
    if button.is_pressed:
        sensor = sensors.DistanceSensor()
        print(sensor.get_distance())
        distance = sensor.get_distance()
        note = 60 + distance
        psonic.play(note,5)
        sleep(0.5)
    else:
        pass
