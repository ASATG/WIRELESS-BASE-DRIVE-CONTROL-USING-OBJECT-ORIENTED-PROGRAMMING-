from machine import Pin, ADC            
from time import sleep                  

potentiometer = ADC(Pin(26))            
potentiometer.atten(ADC.ATTN_11DB)       

while True:
    potentiometer_value = potentiometer.read()
    print(potentiometer_value)
    sleep(0.25)
