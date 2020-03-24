# Logger.py
# Adapted from Adafruit tutorial on MCP9600 I2C Thermocouple
# Modified by Dan Wagner, MIT License

import board
import busio
import adafruit_mcp9600
import codecs

i2c = busio.I2C(board.SCL, board.SDA, frequency=10000)
mcp = adafruit_mcp9600.MCP9600(i2c)


logfile = codecs.open('thermocouple-data.csv', 'a', 'utf-8')
logfile.write(repr(mcp.temperature) + '\n')
logfile.close()