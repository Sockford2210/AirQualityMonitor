import time
from APIInterface import DataService
from AirQuality import Monitor

API_URL = "https://LAPTOP-DQ2OSHGS:32768/api/AirData"
DEVICE_ID = "1"

dataService = DataService(API_URL, DEVICE_ID)
airQualityService = Monitor()
while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if airQualityService.is_data_available():
        reading = airQualityService.take_reading()
        dataService.submit_reading(reading)

    time.sleep(10)
