import board
import busio
import adafruit_scd30
from datetime import datetime
from AirQuality import AirQualityReading

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
FREQUENCY = 50000

class AirQualityMonitor:
    def __init__(self, logger):
        self.logger = logger
        i2c = busio.I2C(board.SCL, board.SDA, frequency=FREQUENCY)
        self.scd = adafruit_scd30.SCD30(i2c)

    def is_data_available(self):
        return self.scd.data_available

    def take_reading(self):
        if self.scd.data_available:
            self.logger.info("Data available on scd board")
            timestamp = datetime.now()
            new_reading = AirQualityReading(self.scd.CO2, self.scd.temperature, self.scd.relative_humidity, timestamp)
            self.logger.info(f"New reading: {new_reading}")
            return new_reading

        else:
            self.logger.error("Data not available on scd board")