import time

SLEEP_TIME_SECONDS = 10

class Monitor:  
    def __init__(self, logger, air_quality_reader, led_interface, data_transfer_service):
        self.logger = logger
        self.air_quality_reader = air_quality_reader
        self.led_interface = led_interface
        self.data_transfer_service = data_transfer_service

    def execute(self):
        try:
            while True:
                # since the measurement interval is long (2+ seconds) we check for new data before reading
                # the values, to ensure current readings.
                if self.air_quality_reader.is_data_available():
                    self.logger.info("Data is available")
                    reading = self.air_quality_reader.take_reading()
                    self.led_interface.turn_green_on()
                    self.data_transfer_service.submit_reading(reading)
                else:
                    self.logger.info("No data is available")

                self.logger.info(f"Sleeping for {str(SLEEP_TIME_SECONDS)} seconds")
                time.sleep(SLEEP_TIME_SECONDS)
        except:
            self.logger.error(f"Process interrupted, terminating")
            self.led_interface.turn_green_off()