from hx711 import HX711

# initialize the HX711 module with the input and output pin numbers
hx = HX711(dout_pin=17, pd_sck_pin=16)

# set the scale factor for the load cell
hx.set_scale(1000)  # 1000 is the scale factor for my load cell

# tare the load cell to zero
hx.tare()

# get the weight from the load cell
weight = hx.get_weight()

print("Weight: {} grams".format(weight))

# set a reference unit if you want to weigh in a specific unit (e.g., grams, ounces)
hx.set_reference_unit(0.1)  # 0.1 gram per unit

# get the weight in ounces
weight_oz = hx.get_weight(ounces=True)

print("Weight: {} ounces".format(weight_oz))
