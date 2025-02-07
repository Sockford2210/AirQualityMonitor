import board
import busio
import adafruit_scd30

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
FREQUENCY = 50000
SCD30_ADDRESS = 0x61

i2c_bus = busio.I2C(board.SCL, board.SDA, frequency=FREQUENCY)
scd30 = adafruit_scd30.SCD30(i2c_bus=i2c_bus, address=SCD30_ADDRESS)