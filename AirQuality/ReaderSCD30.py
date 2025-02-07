from datetime import datetime
from AirQuality.Reading import AirQualityReading
from AirQuality.SCD30Setup import scd30

class AirQualityReader:
    def __init__(self, logger):
        self.__logger = logger
        self.__scd30 = scd30

    def is_data_available(self):
        return self.__scd30.data_available

    def take_reading(self):
        if self.__scd30.data_available:
            self.__logger.info("Data available on SCD30 board")
            timestamp = datetime.now()
            new_reading = AirQualityReading(self.__scd30.CO2, self.__scd30.temperature, self.__scd30.relative_humidity, timestamp)
            self.__logger.info(f"New reading: {new_reading}")
            return new_reading

        else:
            self.__logger.error("Data not available on SCD30 board")