import time
from AirQuality.ReaderSCD30 import AirQualityReader

DATA_READ_ATTEMPTS = 5

class AirQualityMonitor:
    def __init__(self, logger):
        self.__logger = logger

    def execute(self):
        air_quality_reader = AirQualityReader(self.__logger)
        
        # since the measurement interval is long (2+ seconds) we check for new data before reading
        # the values, to ensure current readings.
        if not air_quality_reader.is_data_available():
            raise Exception()
        
        data_read_attempts = 0
        while True:
            if data_read_attempts > DATA_READ_ATTEMPTS:
                raise Exception()

            try:
                reading = air_quality_reader.take_reading()
                return reading
            except:
                data_read_attempts += 1