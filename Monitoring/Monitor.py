import time
from Display.AirQualityModel import AirQualityDisplayModel

SLEEP_TIME_SECONDS = 10
CO2_MIN_WARNING_LIMIT = 2000

class Monitor:  
    def __init__(self, logger, air_quality_reader, data_transfer_service, display):
        self.__logger = logger
        self.__air_quality_reader = air_quality_reader
        self.__data_transfer_service = data_transfer_service
        self.__display = display

    def execute(self):
        try:
            while True:
                # since the measurement interval is long (2+ seconds) we check for new data before reading
                # the values, to ensure current readings.
                if self.__air_quality_reader.is_data_available():
                    self.__logger.info("Data is available")
                    reading = self.__air_quality_reader.take_reading()

                    co2 = reading.get_co2()
                    humidity = reading.get_humidity()
                    temperature = reading.get_temperature()

                    air_quality_display = AirQualityDisplayModel(co2, humidity, temperature)
                    self.__display.update_air_quality_values(air_quality_display)

                    if(float(co2) > CO2_MIN_WARNING_LIMIT):
                        self.__logger.info("CO2 level above safe limit, setting high alert light")
                        self.__display.set_high_co2_alert_light()
                    else:
                        self.__display.unset_high_co2_alert_light()

                    #self.__data_transfer_service.submit_reading(reading)
                else:
                    self.__logger.info("No data is available")

                self.__logger.info(f"Sleeping for {str(SLEEP_TIME_SECONDS)} seconds")
                time.sleep(SLEEP_TIME_SECONDS)
        except Exception as e:
            self.__logger.error(f"Process interrupted, terminating. Error {str(e)}")