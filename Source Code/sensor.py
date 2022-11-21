import time

import board

from adafruit_seesaw.seesaw import Seesaw

class sensor:

    def get_moisture():

        i2c_bus = board.I2C()

        ss = Seesaw(i2c_bus, addr=0x36)

        touch = 0.0
        temp = 0.0

        for i in range(5):    # read moisture level through capacitive touch pad
            touch = touch + float(ss.moisture_read())

            # read temperature from the temperature sensor
            temp = temp + float(ss.get_temp())

            print("temp: " + str(temp) + "  moisture: " + str(touch))
            time.sleep(1)

        touch = touch/5
        temp = temp/5
        return touch
