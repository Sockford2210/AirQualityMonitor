import time
from AirQuality import Monitor

while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    airQualityService = Monitor(frequency)

    time.sleep(0.5)
