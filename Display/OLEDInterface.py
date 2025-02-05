import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = board.I2C()

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

class FourRowOLEDDisplay:
    def reset(self):
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        oled.fill(0)
        oled.show()
    def set_row_one(self, text):
        draw.text((0, 0), text, font=font, fill=255)
    def set_row_two(self, text):
        draw.text((0, 16), text, font=font, fill=255)
    def set_row_three(self, text):
        draw.text((0, 32), text, font=font, fill=255)
    def set_row_four(self, text):
        draw.text((0, 48), text, font=font, fill=255)
    def show(self):
        oled.image(image)
        oled.show()