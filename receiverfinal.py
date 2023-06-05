import network
import espnow
from machine import UART
from bd import BaseDrive

def espnow_rx():
    uart = UART(0, baudrate=115200)

    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()                

    e = espnow.ESPNow()                  
    e.active(True)

    peer = b'\xa4\xe5\x7c\xf5\x85\x7c'   
    e.add_peer(peer)                     
    b = BaseDrive(5,4,13,17,16,12)
    while True:
        host, msg = e.recv()
        dire,pot = map(int,msg.split())
        speed = (pot*100)/4096
        if(dire == 0):
            b.left(speed)
        if(dire == 1):
            b.forward(speed)
        if(dire == 2):
            b.backward(speed)
        if(dire == 3):
            b.right(speed)
        if(dire == 4):
            b.stop()
        

if __name__ == "__main__":
    espnow_rx()
