import RPi.GPIO as IO
import time;

class CommandControl:
  def __init__():
    self.command_to_pin = { 
      "front": 19, 
    } 
    IO.setwanrings(False)
    IO.setmode(IO.BCM)

  def gpio_process(self, command):
    gpio_pin_no = self.command_to_pin.get(command, None)
    print(gpio_pin_no)
    if(gpio_pin_no is not None):
      IO.setup(gpio_pin_no, IO.OUT)
      PIN = IO.PWM(gpio_pin_no, 100)
      PIN.start(70)
      time.sleep(2)