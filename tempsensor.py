#!/usr/bin/env python

import time
from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()

while True:
    temperature_in_all_units = sensor.get_temperatures([Unit.DEGREES_C, Unit.DEGREES_F, Unit.KELVIN])
    print("The temperature is %s celsius" % temperature_in_all_units[0])
    time.sleep(1)

