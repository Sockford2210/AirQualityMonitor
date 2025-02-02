import RPi.GPIO as GPIO
green_led_pin = 24

class LEDInterface:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(green_led_pin, GPIO.OUT)
        GPIO.output(green_led_pin, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()

    def turn_green_on(self):
        GPIO.output(green_led_pin, GPIO.HIGH)
    
    def turn_green_off(self):
        GPIO.output(green_led_pin, GPIO.LOW)