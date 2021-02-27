from time import sleep
from sense_hat import SenseHat
import random
import sys
import time

import cv2
from lobe import ImageModel

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

go = [
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, r, r, e, e, e, r, e,
   r, e, e, e, e, r, e, r,
   r, e, r, r, e, r, e, r,
   r, e, e, r, e, r, e, r,
   e, r, r, e, e, e, r, e,
   e, e, e, e, e, e, e, e
]


options =dict([('paper',paper), ('scissors',scissors), ('rock', rock)])
hat = SenseHat()
cam = cv2.VideoCapture(0)

def startCountDown(f):
    for i in range(f,0,-1):
      print(str(i))
      hat.show_letter(str(i),r)
      sleep(0.5)
    hat.clear()
    hat.set_pixels(go)
    print('GO!!!')
    sleep(0.75)

def playRockSciccorsPaper(times,model):
  for i in range(times,0,-1):
    sleep(0.5)
    hat.clear()
    startCountDown(3)
    key, value = random.choice(list(options.items()))
    print(key)

    result = model.predict_from_file('capture.jpg')
    print(result.prediction)
    if result.prediction == key:
      print("WIN")
    else:
      print("LOSE")
    hat.set_pixels(value)
    sleep(0.75)


def main():
  print("Initializing, please wait...")
  model = ImageModel.load("model")
  print("Initializing is completed. Press up to start...")
  hat.clear()
  while True:
    s, image = cam.read()
    cv2.imwrite("capture.jpg",image)
    for event in hat.stick.get_events():
      if event.action == "pressed":
        if event.direction == "up":
          print('Let\'s play Rock-Scissors-Paper')
          playRockSciccorsPaper(3,model)
          hat.clear()
          print('This round is completed. Press up to play again.')
        else:
          print("Terminating application, please wait...")
          sys.exit(0)


  cam.release()


if __name__ == "__main__":
    main()