from machine import Pin,UART
from time import sleep
button = Pin(14,Pin.IN,Pin.PULL_UP)
button2 = Pin(15,Pin.IN,Pin.PULL_UP)
uart = UART(1,9600,rx=Pin(5),tx=Pin(4))
led = Pin(25,Pin.OUT)
led.value(1)
while True:
    if button.value()==0:
        uart.write("rd")
        print('sent')
        sleep(0.5)
        
    if button2.value()==0:
        sleep(0.5)
        uart.write("ru")
        print('sent2')
        
    
    #if uart.any():
        #data = uart.read().decode('utf-8').strip()
        
        
        
        
        