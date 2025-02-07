import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = board.I2C()

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

class FourRowOLEDDisplay:
    def __init__(self):
        self.__oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

    def reset(self):
        self.__image = Image.new("1", (self.__oled.width, self.__oled.height))
        self.__draw = ImageDraw.Draw(self.__image)
        self.__oled.fill(0)
        self.__oled.show()

    def set_row_one(self, text):
        self.__draw.text((0, 0), text, font=font, fill=255)

    def set_row_two(self, text):
        self.__draw.text((0, 16), text, font=font, fill=255)

    def set_row_three(self, text):
        self.__draw.text((0, 32), text, font=font, fill=255)

    def set_row_four(self, text):
        self.__draw.text((0, 48), text, font=font, fill=255)

    def show(self):
        self.__oled.image(self.__image)
        self.__oled.show()