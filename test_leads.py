import board
import busio
import adafruit_mcp9600
import time

i2c = busio.I2C(board.SCL, board.SDA, frequency=10000)
mcp = adafruit_mcp9600.MCP9600(i2c)


while True:
	print("Hot lead: {}".format(mcp.temperature))
	print("Ambient: {}".format(mcp.ambient_temperature))
	time.sleep(1)
