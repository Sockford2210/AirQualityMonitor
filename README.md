# Transfer Files to RaspberryPi
Open a command line window from this directory and run:
scp .\{filename} admin@{ip}:.\AirSensor

# Run on RaspberryPi
ssh into raspberry pi run the following commands:
Create python virtual environment: *python3 -m venv .venv*
Activate virual environment: *source .venv/bin/activate*
Install python3 setup tools: *pip3 install --upgrade setuptools*
Install cictuipython library *pip3 install --upgrade adafruit-python-shell*
Install adafruit scd30 library tools: *pip3 install --upgrade adafruit-circuitpython-scd30*
Install python3: *sudo apt-get install python3-pip*
Install python3 setup tools: *sudo pip3 install --upgrade setuptools*