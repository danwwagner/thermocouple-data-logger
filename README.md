# thermocouple-data-logger
Research code for Agronomy thermocouple data logging mechanism, Spring 2020.

## Installation
1. Load a Raspberry Pi with the latest Raspbian version.
2. Connect to the Internet.
3. Install python3-pip if needed.
4. Modify /boot/config.txt to read: dtparam=i2c_arm=on,i2c_arm_baudrate=10000 to adjust baud.
5. Enable I2C interfacing via the raspi-config utility.
6. Install the MCP9600 library: pip3 install adafruit-circuitpython-mcp9600 (if not already). 