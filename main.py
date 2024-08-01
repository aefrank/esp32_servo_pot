''' IMPORTS '''

from machine import Pin, ADC
from time import sleep

try:
    from servo import Servo
except ImportError:
    from wifi_utils import connect
    connect("UCSD-Conferences", "Conferences2024")
    mip.install('github:pvanallen/esp32-getstarted/examples/servo.py')
    from servo import Servo

''' MAIN '''

def main():
    pot = ADC(Pin(34))
    pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

    servo = Servo(18)

    while True:
      pot_value = pot.read()
      degrees = int(180.0 / 4095.0 * pot_value)
      print(f"Input: {pot_value}\tServo angle: {degrees}")
      servo.write_angle(degrees)
      sleep(0.1)




if __name__=='__main__':
    main()