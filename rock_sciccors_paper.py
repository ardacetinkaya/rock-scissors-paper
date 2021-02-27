from time import sleep
from sense_hat import SenseHat
import random

e = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
y = (255, 255, 0)

scissors = [
   e, e, e, e, e, e, r, e,
   r, r, e, e, e, r, e, e,
   r, r, e, e, r, e, e, e,
   e, e, r, r, e, e, e, e,
   e, e, r, r, e, e, e, e,
   r, r, e, e, r, e, e, e,
   r, r, e, e, e, r, e, e,
   e, e, e, e, e, e, r, e
]

paper = [
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, r, r, r, r, r, r, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e
]

rock = [
   e, e, e, e, e, e, e, e,
   e, e, e, r, e, e, e, e,
   e, e, r, r, r, r, e, e,
   e, e, r, r, r, r, r, e,
   e, r, r, r, r, r, e, e,
   e, r, r, r, r, r, e, e,
   e, e, r, r, r, e, e, e,
   e, e, e, e, e, e, e, e
]


options =dict([('paper',paper), ('scissors',scissors), ('rock', rock)])
hat = SenseHat()

def startCountDown(f):
    for i in range(f,0,-1):
      print(str(i))
      hat.show_letter(str(i),r)
      sleep(0.5)
    print('GO!!!')

def playRockSciccorsPaper(times):
  for i in range(times,0,-1):
    sleep(0.5)
    hat.clear()
    startCountDown(3)
    key, value = random.choice(options.items())
    print(key)
    hat.set_pixels(value)
    sleep(0.75)

hat.clear()
while True:
  for event in hat.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        print('Let''s play Rock-Scissors-Paper')
        playRockSciccorsPaper(3)
        hat.clear()
        print('This rount is completed. Press up to play again.')


