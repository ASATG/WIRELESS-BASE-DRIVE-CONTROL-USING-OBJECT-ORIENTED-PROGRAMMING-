from machine import Pin, ADC 
from time import sleep
import network
import espnow
import time

push_button0 = Pin(25, Pin.IN)
push_button1 = Pin(34, Pin.IN)
push_button2 = Pin(35, Pin.IN)
push_button3 = Pin(32, Pin.IN)
push_button4 = Pin(33, Pin.IN)
potentiometer = ADC(Pin(26))            
potentiometer.atten(ADC.ATTN_11DB)

sta = network.WLAN(network.STA_IF)    
sta.active(True)
sta.disconnect()        

e = espnow.ESPNow()     
e.active(True)

peer1 = b'\xb0\xb2\x1c\xa7\x74\x60'   
e.add_peer(peer1)



while(True):
    dir = 4
    l0 = push_button0.value()
    l1 = push_button1.value()
    l2 = push_button2.value()
    l3 = push_button3.value()
    l4 = push_button4.value()
    potentiometer_value = potentiometer.read()
    if l0 == True:
        dir = 0
    if l1 == True:
        dir = 1
    if l2 == True:
        dir = 2
    if l3 == True:
        dir = 3
    if l4 == True:
        dir = 4
    sendstr = str(dir) + " " + str(potentiometer_value)
    
    e.send(peer1, sendstr, True)     
    
