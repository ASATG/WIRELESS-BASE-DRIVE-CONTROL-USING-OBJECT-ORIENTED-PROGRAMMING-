from dcmotor import DCMotor       
from machine import Pin, PWM   
from time import sleep     
frequency = 15000

pin1 = Pin(32, Pin.OUT)    
pin2 = Pin(33, Pin.OUT)     
enable1 = PWM(Pin(13), frequency)
dc_motor1 = DCMotor(pin1, pin2, enable1)      
dc_motor1 = DCMotor(pin1, pin2, enable1, 350, 1023)

pin3 = Pin(25, Pin.OUT)    
pin4 = Pin(26, Pin.OUT)     
enable2 = PWM(Pin(14), frequency) 
dc_motor2 = DCMotor(pin3, pin4, enable2)      
dc_motor2 = DCMotor(pin3, pin4, enable2, 350, 1023)

dc_motor1.forward(20)
dc_motor2.forward(20)
sleep(5)
dc_motor1.backwards(20)
dc_motor2.backwards(20)
sleep(5)       
    

