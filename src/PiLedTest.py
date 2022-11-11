import socket
import time
from time import sleep


from hal import hal_input_switch as switch
from hal import hal_led as led



def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)



def main():
    led.init()
    switch.init()
while(1):
    if(switch.read_slide_switch()==1):
        blink_led(0.2)
    elif(switch.read_slide_switch()==0):
        i=0
        for i in range(25):
         blink_led(0.1)
        led.set_output(0.0)























if __name__ == "__main__":
    main()