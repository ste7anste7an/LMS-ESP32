# LMS-ESP32 Testing

## How testing is performed

After production of the LMS-ESP32 board, an acceptance test needs to be performed
 that tests all the GPIO pins for good connection and checks for short circuits with 
surrounding pins. In each tests, two units are involved: the Tester unit, and the Device Under Test (DUT). The Tester unit is run in and endless loop and can serve testing of multple DUT's.

The Tester unit is fitted with a NeoPixel Led connected to GPIO32.
 The NeoPixel indicates the state of the test.
- Orange: a new DUT can be inserted
- Green: 1 second, test succeeded succesfully
- Red: 5 brief flashes, test failed.

During test serial output is provided on the Tester unit. This shows per DUT the following information (if the test is successful):
```
*********************
* Ready for testing *
* Insert DUT in rig *
*********************
[*] Testing ID 4c11ae6464c0
[*] Test passed succesfully

```

If a test failes, the following information is (typically) shown. In this case, GPIO4 and GPIO5 were not connected:
```
*********************
* Ready for testing *
* Insert DUT in rig *
*********************
[*] Testing ID 4c11ae6464c0

[!] Error when setting pin GP05 high

[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [X]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [.]  [.]  [.]  [1]  [.]  [.]  [.]  [.] 

[!] Error when setting pin GP04 high

[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [.]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [X]  [.]  [.]  [1]  [.]  [.]  [.]  [.] 

[!] Error when setting pin GP05 low

[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [X]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [.]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 

[!] Error when setting pin GP04 low

[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [.]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [X]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 

[!] Test failed with 4 error(s)

```

In case there is a short circuit of neigboring pins,
 the following output is shown (GPIO4 and GPIO5 are 
short circuited, hence the 'S' is indicated):
```
*********************
* Ready for testing *
* Insert DUT in rig *
*********************
[*] Testing ID 4c11ae6464c0

[!] Error when setting pin GP05 high
[!] One or more pins are short circuited (S=short, .=ok, X=not connected, V=ok, 1=always high)


[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [V]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [S]  [.]  [.]  [1]  [.]  [.]  [.]  [.] 

[!] Error when setting pin GP04 high
[!] One or more pins are short circuited (S=short, .=ok, X=not connected, V=ok, 1=always high)


[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [S]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [V]  [.]  [.]  [1]  [.]  [.]  [.]  [.] 

[!] Error when setting pin GP05 low
[!] One or more pins are short circuited (S=short, .=ok, X=not connected, V=ok, 1=always high)


[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [V]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [S]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 

[!] Error when setting pin GP04 low
[!] One or more pins are short circuited (S=short, .=ok, X=not connected, V=ok, 1=always high)


[*] -------------------------------------
[*] GP05 GP22 GP25 GP02 GP26 GP27 GP32 GP33 
[*]  [S]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 
[*] GP04 GP21 GP23 GP00 GP12 GP13 GP14 GP15 
[*]  [V]  [.]  [.]  [.]  [.]  [.]  [.]  [.] 

[!] Test failed with 4 error(s)

```


1) Handshake

The Tester and DUT are connected 
The firmware for testing is the same as the production firmware. The DUT 
checks for the presence of the tester unit by sending `start`
2) test all pins high
3) test all pins low
 
Go to the [LMS-ESP32 Web Based installer](https://ste7anste7an.github.io/LMS-ESP32/).
