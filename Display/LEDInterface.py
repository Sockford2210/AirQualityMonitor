import RPi.GPIO as GPIO

GREEN_LED_PIN_NUMBER = 24
RED_LED_PIN_NUMBER = 23

class LEDInterface:
    def __init__(self, logger):
        self.__logger = logger
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GREEN_LED_PIN_NUMBER, GPIO.OUT)
        GPIO.output(GREEN_LED_PIN_NUMBER, GPIO.LOW)
        GPIO.setup(RED_LED_PIN_NUMBER, GPIO.OUT)
        GPIO.output(RED_LED_PIN_NUMBER, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()

    def turn_green_on(self):
        try:
            GPIO.output(GREEN_LED_PIN_NUMBER, GPIO.HIGH)
            self.__logger.info("Green LED turned ON")
        except:
            self.__logger.error(f"Green LED, pin: {str(GREEN_LED_PIN_NUMBER)} failed to turn on")
    
    def turn_green_off(self):
        try:
            GPIO.output(GREEN_LED_PIN_NUMBER, GPIO.LOW)
            self.__logger.info("Green LED turned OFF")
        except:
            self.__logger.error(f"Green LED, pin: {str(GREEN_LED_PIN_NUMBER)} failed to turn off")

    def turn_red_on(self):
        try:
            GPIO.output(RED_LED_PIN_NUMBER, GPIO.HIGH)
            self.__logger.info("Red LED turned ON")
        except:
            self.__logger.error(f"Red LED, pin: {str(RED_LED_PIN_NUMBER)} failed to turn on")
    
    def turn_red_off(self):
        try:
            GPIO.output(RED_LED_PIN_NUMBER, GPIO.LOW)
            self.__logger.info("Red LED turned OFF")
        except:
            self.__logger.error(f"Red LED, pin: {str(RED_LED_PIN_NUMBER)} failed to turn off")