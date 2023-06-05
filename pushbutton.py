from machine import Pin
from time import sleep

push_button0 = Pin(25, Pin.IN)
push_button1 = Pin(34, Pin.IN)
push_button2 = Pin(35, Pin.IN)
push_button3 = Pin(32, Pin.IN)
push_button4 = Pin(33, Pin.IN)

while True:
    l0 = push_button0.value()
    l1 = push_button1.value()
    l2 = push_button2.value()
    l3 = push_button3.value()
    l4 = push_button4.value()
    if l0 == True:
        print(0)
    if l1 == True:
        print(1)
    if l2 == True:
        print(2)
    if l3 == True:
        print(3)
    if l4 == True:
        print(4)
