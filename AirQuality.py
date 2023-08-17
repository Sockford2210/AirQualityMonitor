import board
import busio
import adafruit_scd30
from datetime import datetime

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
FREQUENCY = 50000

class AirQualityReading:
    def __init__(self, co2, temperature, humidity, timestamp):
        self.co2 = co2
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp

    def __str__(self):
        return f"[{self.timestamp}] - CO2: {self.co2} ppm; Temperature: {self.temperature} degrees C; Humidity: {self.humidity} %%rH"

class Monitor:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=FREQUENCY)
        self.scd = adafruit_scd30.SCD30(i2c)

    def is_data_available(self):
        return self.scd.data_available

    def take_reading(self):
        if self.scd.data_available:
            print("Data Available\n")
            timestamp = datetime.now()
            newReading = AirQualityReading(self.scd.CO2, self.scd.temperature, self.scd.relative_humidity, timestamp)
            print(newReading)
            print("")
            return newReading

        else:
            print("ERROR: Data Not Available!\n")