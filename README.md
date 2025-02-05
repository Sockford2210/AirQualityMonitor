# Transfer Files to RaspberryPi
Open a command line window from this directory and run:
scp .\{filename} admin@{ip}:.\AirSensor

To copy all files from directory:
scp -r .\* admin@{ip}:.\AirSensor

# Run on RaspberryPi
ssh into raspberry pi run the following commands:
Install python3: *sudo apt-get install python3-pip*
Create python virtual environment: *python3 -m venv .venv*
Activate virual environment: *source .venv/bin/activate*
Install python3 setup tools: *pip3 install --upgrade setuptools*
Install cictuipython library *pip3 install --upgrade adafruit-python-shell*
Install adafruit ssd1306 library tools: *pip3 install --upgrade pillow*
Install adafruit scd30 library tools: *pip3 install --upgrade adafruit-circuitpython-scd30*
Install adafruit ssd1306 library tools: *pip3 install --upgrade adafruit-circuitpython-ssd1306*

I2c bus addresses:
SCD30: 61
Display: 3c

Python Libraries:
Adafruit_CicruitPython_SSD1306: https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/
Adafruit_CircuitPython_SCD30: https://github.com/adafruit/Adafruit_CircuitPython_SCD30
Pillow: https://pillow.readthedocs.io/en/stable/