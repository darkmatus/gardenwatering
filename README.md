Installing needed Software:

```
cd /tmp \
&& sudo apt install pkg-config libusb-dev python python-pip python-openssl git -y \
&& git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT \
&& sudo python setup.py install \
&& cd /tmp \
&& wget -O sispmctl.tar.gz https://sourceforge.net/projects/sispmctl/files/latest/download \
&& tar xzvf sispmctl.tar.gz \
&& cd sispmctl-4.1 && ./configure && make && sudo make install \
&& sudo ldconfig
&& sudo echo 'pi ALL=NOPASSWD:/usr/local/bin' >> /etc/sudoers \
&& sudo pip install --upgrade RPi.GPIO
```