import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=5, pd_sck_pin=6)
# hx.set_reading_format("MSB", "MSB")
# hx.set_reference_unit(92)
# hx.reset()
# hx.tare()

while True:
    #reading = hx.get_raw_data_mean()
    #print(reading)
    val = hx.get_weight()
    print(val)

    # https://www.youtube.com/watch?v=FdFXlTdpueQ