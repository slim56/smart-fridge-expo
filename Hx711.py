import RPi.GPIO as GPIO
from hx711 import HX711
from time import sleep

#hx = HX711(dout_pin=17, pd_sck_pin=16)
#hx.set_reading_format("MSB", "MSB")
#hx.set_reference_unit(92)
#hx.reset()
#hx.tare()

#while True:
    #val = hx.get_weight()
    #print(val)
try:
    hx711 = HX711(
        dout_pin = 17,
        pd_sck_pin = 16,
        channel = 'B',
        gain = 32
        )

    hx711.reset()
    measures = hx711.get_raw_data(times=5)
    '''
    for i in range (5):
        if measures[i]<measures[0]:
            while measures[i]<measures[0]:
                measures[i] = measures[i]+ 1
                 '''
    kw = int(input("Enter known weight: "))
    calb_factor = []
    for measure in measures:
        calb_factor.append(((measure/kw)))

    calb_factor = ((sum(calb_factor))/(len(calb_factor)))
    print((int(calb_factor)))
    
    while True:
        fir = (( (sum((hx711.get_raw_data(times= 5)))/5))/calb_factor)
        #sec = (( (sum(hx711.get_raw_data(times= 20)))/20)/calb_factor)
        print(((fir)))#+sec)/2))
        hx711.reset()
        
        print(hx711.get_raw_data(times=2))
        sleep(2)

finally:
    GPIO.cleanup()


