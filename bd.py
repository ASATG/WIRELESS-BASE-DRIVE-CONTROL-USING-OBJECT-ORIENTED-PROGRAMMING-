from dcmotor import DCMotor       
from machine import Pin, PWM   
from time import sleep

class BaseDrive:
    def __init__(self,pin1,pin2,pwm1,pin3,pin4,pwm2):
        self.frequency = 15000
        
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)     
        self.enable1 = PWM(Pin(pwm1), self.frequency)
        self.dc_motor1 = DCMotor(self.pin1, self.pin2, self.enable1)      
        self.dc_motor1 = DCMotor(self.pin1, self.pin2, self.enable1, 350, 1023)
        
        self.pin3 = Pin(pin3, Pin.OUT)    
        self.pin4 = Pin(pin4, Pin.OUT)     
        self.enable2 = PWM(Pin(pwm2), self.frequency) 
        self.dc_motor2 = DCMotor(self.pin3, self.pin4, self.enable2)      
        self.dc_motor2 = DCMotor(self.pin3, self.pin4, self.enable2, 350, 1023)
        
    def forward(self,speed):
        self.dc_motor1.forward(speed)
        self.dc_motor2.forward(speed)
        
    def backward(self,speed):
        self.dc_motor1.backwards(speed)
        self.dc_motor2.backwards(speed)
        
    def left(self,speed):
        self.dc_motor1.backwards(speed)
        self.dc_motor2.forward(speed)
        
    def right(self,speed):
        self.dc_motor1.forward(speed)
        self.dc_motor2.backwards(speed)
        
    def stop(self):
        self.dc_motor1.stop()
        self.dc_motor2.stop() 
        
b = BaseDrive(5,4,13,17,16,14)
b.forward(20)
sleep(5)
b.backward(20)
sleep(5)
b.left(20)
sleep(5)
b.right(20)
sleep(5)
b.stop()

