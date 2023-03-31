# DUT

from machine import UART,Pin,unique_id
from time import ticks_ms,ticks_diff
from binascii import hexlify
from time import sleep_ms

pins = [5,22,25,2,26,27,32,33,4,21,23,0,12,13,14,15]
pin_led = 32
rx_pin=18
tx_pin=19
baudrate=115200
uart=UART(1,baudrate=baudrate,rx=rx_pin,tx=tx_pin,timeout=1)


def wait_for_ack():
    start = ticks_ms()
    ack=False
    while ticks_diff(ticks_ms(), start) < 1000 and not ack:
        a=uart.read()
        ack = a==b'ack'
    return ack

def write_gpio(pin,val):
    p = Pin(pin, Pin.OUT)
    p.value(val)
    
def test_pin(pin,state=1):
    # set Pin(pin) high, other low
    for p in pins:
        write_gpio(p,1-state)
    write_gpio(pin,state)
    if state==1:
        s='H'
    else:
        s='L'
    uart.write(s+"%02d"%pin)
    ack=wait_for_ack()
    if not ack:
        print('time out')

def write_id():
    id=hexlify(unique_id())
    uart.write(b"ID="+id)
    ack=wait_for_ack()
    
def test_program():
    print("start test program")
    write_id()
    for p in pins:
        test_pin(p,state=1)
    for p in pins:
        test_pin(p,state=0)
    # set pin_led to read
    Pin(pin_led, Pin.IN)
        
    uart.write('stop')
    
sleep_ms(200) # wait    
start = ticks_ms()
uart.read() # empty read buf
uart.write('start')
ack=False
while ticks_diff(ticks_ms(), start) < 1000 and not ack:
    a=uart.read()
    ack = a==b'ack'
if ack:
    test_program()
else:
    print('continue')