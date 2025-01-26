import time
from APIInterface import DataTransferService
from AirQualityMock import AirQualityMonitor
from SystemLogging import file_logger as logger

API_URL = "https://LAPTOP-DQ2OSHGS:32768/api/AirData"
DEVICE_ID = "1"
SLEEP_TIME_SECONDS = 10

transfer = DataTransferService(API_URL, DEVICE_ID, logger)
monitor = AirQualityMonitor(logger)
while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if monitor.is_data_available():
        logger.info("Data is available")
        reading = monitor.take_reading()
        transfer.submit_reading(reading)
    else:
        logger.info("No data is available")

    try:
        logger.info(f"Sleeping for {str(SLEEP_TIME_SECONDS)} seconds")
        time.sleep(SLEEP_TIME_SECONDS)
    except:
        logger.error(f"Sleep interrupted, terminating")
        break