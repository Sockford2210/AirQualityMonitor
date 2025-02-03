import RPi.GPIO as GPIO

GREEN_LED_PIN_NUMBER = 24

class LEDInterface:
    def __init__(self, logger):
        self.logger = logger
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GREEN_LED_PIN_NUMBER, GPIO.OUT)
        GPIO.output(GREEN_LED_PIN_NUMBER, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()

    def turn_green_on(self):
        try:
            GPIO.output(GREEN_LED_PIN_NUMBER, GPIO.HIGH)
            self.logger.info("Green LED turned ON")
        except:
            self.logger.error(f"Green LED, pin: {str(GREEN_LED_PIN_NUMBER)} failed to turn on")
    
    def turn_green_off(self):
        try:
            GPIO.output(GREEN_LED_PIN_NUMBER, GPIO.LOW)
            self.logger.info("Green LED turned OFF")
        except:
            self.logger.error(f"Green LED, pin: {str(GREEN_LED_PIN_NUMBER)} failed to turn off")