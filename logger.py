# Logger.py
# Adapted from Adafruit tutorial on MCP9600 I2C Thermocouple
# Modified by Dan Wagner, MIT License

import board
import busio
import adafruit_mcp9600
import codecs
import time

LOG_INTERVAL = 60
FILENAME = 'thermocouple-data.csv'
i2c = busio.I2C(board.SCL, board.SDA, frequency=10000)
mcp = adafruit_mcp9600.MCP9600(i2c)

# Start the session with a newline demarkation
logfile = codecs.open(FILENAME, 'a', 'utf-8')
logfile.write('\n')
logfile.close()

# Record temperature on the hot end of the thermocouple every LOG_INTERVAL
while True:
	logfile = codecs.open(FILENAME, 'a', 'utf-8')
	logfile.write(repr(mcp.temperature) + '\n')
	logfile.close()
	time.sleep(LOG_INTERVAL)
