class LEDInterface:
    def __init__(self, logger):
        self.logger = logger

    def turn_green_on(self):
        self.logger.info("GREEN LED ON")
    
    def turn_green_off(self):
        self.logger.info("GREEN LED OFF")