import time
from DataTransfer.TransferService import DataTransferService
from AirQuality.ReaderSCD30 import AirQualityReader
from Display.LEDInterface import LEDInterface
from SystemLogging import console_logger as logger

API_URL = "https://LAPTOP-DQ2OSHGS:32768/api/AirData"
DEVICE_ID = "1"
SLEEP_TIME_SECONDS = 10

#transfer = DataTransferService(API_URL, DEVICE_ID, logger)
air_quality_reader = AirQualityReader(logger)
led = LEDInterface(logger, GREEN_LED_PIN_NUMBER)

try:
    while True:
        # since the measurement interval is long (2+ seconds) we check for new data before reading
        # the values, to ensure current readings.
        if air_quality_reader.is_data_available():
            logger.info("Data is available")
            reading = air_quality_reader.take_reading()
            led.turn_green_on()
            #transfer.submit_reading(reading)
        else:
            logger.info("No data is available")

        logger.info(f"Sleeping for {str(SLEEP_TIME_SECONDS)} seconds")
        time.sleep(SLEEP_TIME_SECONDS)
except:
    logger.error(f"Process interrupted, terminating")
    led.turn_green_off()
    #del transfer
    del led
    del monitor