# asmo - a serial monitor online #
This is the easiest way to send and receive data to/from your serial adapter using a webfrontend.
Basic idea was a way to interact and debug with an arduino in a local network.

## Requirements ##
This software has been developed with Python 2.7 and needs pySerial, ConfigParser and Bottle.  
Using EasyInstall, you can run ``easy_install pySerial configparser bottle``

## Configuration ##
To configure it, copy the example.conf and rename it to config.conf. The options should be rather self-explaning.
After setting up asmo, run app.py to start the webserver

#### Webserver [server] ####
host - hostname (default "localhost")  
port - port of the webserver (default 8080)

#### Serial Connection [serial] ####
serial - path to your serial adapter  
baud - baud-rate