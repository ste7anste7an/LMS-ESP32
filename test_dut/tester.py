# tester

from machine import UART,Pin
from neopixel import NeoPixel
from time import sleep_ms

pins = [5,22,25,2,26,27,32,33,4,21,23,0,12,13,14,15]

tx_pin=19
rx_pin=18
baudrate=115200
uart=UART(1,baudrate=baudrate,rx=rx_pin,tx=tx_pin,timeout=1)

def all_pins_in():
    for p in pins:
        pin = Pin(p, Pin.IN, pull=Pin.PULL_DOWN)
        

def test_pin(pin_test,state=1):
    errors=[]
    vals={}
    for p in pins:
        pin = Pin(p, Pin.IN, pull=Pin.PULL_DOWN)
        val=pin.value()
        vals[p]=val
    #print("vals",vals)
    test_result=0
    for p in pins:
        if p==pin_test:
            test_result+=not vals[p]==state
        else:
            test_result+=not (vals[p]==1-state)
    #print("test_result",test_result)
    return test_result
            
# wait for start message from DUT
while True:
  all_pins_in()
  start=False
  while not start:
      msg=uart.read()
      if msg==b'start':
          start=True
  uart.write('ack')
  print("start testing")
  testing=True
  test_result=0
        
  while testing:
    r=uart.read()
    if r:
        r=r.decode('ascii')
        print("rcv",r)
        if len(r)>=1:
            if r=='stop':
                testing=False
            if r[0]=='H':
                pin=int(r[1:])
                print("test pin high",pin)
                test_result+=test_pin(pin,state=1)
                uart.write('ack')
            if r[0]=='L':
                pin=int(r[1:])
                print("test pin low",pin)
                test_result+=test_pin(pin,state=0)
                uart.write('ack')
            if r[0]=='I':
                print("ID=",r.split('=')[1])
                uart.write('ack')
  print("test finished")
  print("test_result=",test_result)
  np=NeoPixel(Pin(32),1)
  if test_result>0:
      np[0]=(100,0,0)
  else:
      np[0]=(0,100,0)
  np.write()
  sleep_ms(1000)
  np[0]=(0,0,0)
  np.write()
Pin(32,Pin.IN)
