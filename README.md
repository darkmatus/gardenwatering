# gardenwatering
Python project for a garden watering system based on a raspberry pi (3B+), DHT22, HL-83 and a EnerGenie Programmable power strip (EG-PM2)

# Installing needed Software

`cd /tmp \
&& sudo apt install pkg-config libusb-dev python python-pip python-openssl git -y \
&& git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT \
&& sudo python setup.py install \
&& cd /tmp \
&& wget -O sispmctl.tar.gz https://sourceforge.net/projects/sispmctl/files/latest/download \
&& tar xzvf sispmctl.tar.gz \
&& cd sispmctl-4.1 && ./configure && make && sudo make install \
&& sudo ldconfig
&& sudo echo 'pi ALL=NOPASSWD:/usr/local/bin' >> /etc/sudoers \
&& sudo pip install --upgrade RPi.GPIO`

# Cron Runs
## Database Cleanup
Database cleanup runs every day 1 AM.
`0 1 * * * /usr/bin/python /home/pi/garden/watering/cleanup.py >/dev/null 2>&1`

## Pump Controll
The Pump Controll Check is the part of the software which switch the power of the pump on, and after 5 minutes off.
The Cron runs every day 8 PM 
`0 20 * * * /usr/bin/python /home/pi/garden/watering/pump.py >/dev/null 2>&1`

# Software as System Service
 The main part (the temperature and rain check part) should be run as a service.
 This can be done as followed:
 `touch /etc/systemd/system/weatherCheck.service`
` [Unit]
  Description=weather check service
  After=network.target
  StartLimitIntervalSec=0
  [Service]
  Type=simple
  Restart=always
  RestartSec=1
  User=pi
  ExecStart=/usr/bin/python /home/pi/garden/watering/main.py
  
  [Install]
  WantedBy=multi-user.target
`

Start the service:
`systemctl start weatherCheck`
Enable the service:
`systemctl enable weatherCheck`
