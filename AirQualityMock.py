import random
from datetime import datetime
from AirQuality import AirQualityReading

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
FREQUENCY = 50000

class AirQualityMonitor:
    def __init__(self, logger):
        self.logger = logger

    def is_data_available(self):
        return True

    def take_reading(self):
        self.logger.info("Data Available")

        timestamp = datetime.now()
        co2 = random.randint(500, 700)
        temperature = random.randint(18, 30)
        relative_humidity = random.randint(45, 65)

        new_reading = AirQualityReading(co2, temperature, relative_humidity, timestamp)
        self.logger.info(f"New reading: {new_reading}")
        return new_reading