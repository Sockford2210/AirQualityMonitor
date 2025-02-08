import time
from Display.AirQualityModel import AirQualityDisplayModel
from Monitoring.AirQualityMonitor import AirQualityMonitor

SLEEP_TIME_SECONDS = 10
CO2_MIN_WARNING_LIMIT = 2000
DATA_READ_ATTEMPTS = 5

class Monitor:  
    def __init__(self, logger, data_transfer_service, display):
        self.__logger = logger
        self.__data_transfer_service = data_transfer_service
        self.__display = display

    def execute(self):
        try:
            air_quality_monitor = AirQualityMonitor(self.__logger)
            while True:
                reading = air_quality_monitor.execute()

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

                self.__logger.info(f"Sleeping for {str(SLEEP_TIME_SECONDS)} seconds")
                time.sleep(SLEEP_TIME_SECONDS)
        except Exception as e:
            self.__logger.error(f"Process interrupted, terminating. Error {str(e)}")