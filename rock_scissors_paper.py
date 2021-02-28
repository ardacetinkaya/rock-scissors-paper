from time import sleep
from sense_hat import SenseHat
import random
import sys
import time
from PIL import Image

import cv2
from lobe import ImageModel

e = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
y = (255, 255, 0)
g = (155, 255, 155)

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

win = [
   g, g, g, g, g, g, g, g,
   g, g, g, g, g, g, g, e,
   g, g, g, g, g, g, e, g,
   g, g, g, g, g, e, g, g,
   e, g, g, g, e, g, g, g,
   g, e, g, e, g, g, g, g,
   g, g, e, g, g, g, g, g,
   g, g, g, g, g, g, g, g
]

lose = [
   r, r, r, r, r, r, r, r,
   r, e, r, r, r, r, e, r,
   r, r, e, r, r, e, r, r,
   r, r, r, e, e, r, r, r,
   r, r, r, e, e, r, r, r,
   r, r, e, r, r, e, r, r,
   r, e, r, r, r, r, e, r,
   r, r, r, r, r, r, r, r
]


HAT = SenseHat()
CAM = cv2.VideoCapture(0)
OPTIONS =dict([
  ('paper',paper), 
  ('scissors',scissors), 
  ('rock', rock)])

def startCountDown(_from, _round):
    for i in range(_from,0,-1):
      print(str(i))
      HAT.show_letter(str(i),r)
      sleep(0.5)

    HAT.clear()
    HAT.set_pixels(go)
    print('GO!!!')

def playRockSciccorsPaper(_times, _model):
  for i in range(_times,0,-1):
    sleep(0.5)
    HAT.clear()
    startCountDown(3,i)
    sleep(0.75)
    key, value = random.choice(list(OPTIONS.items()))
    print("PI\'s choice is {choice}".format(choice=key))
    s, image = CAM.read()
    cv2.imwrite("capture_{index}.jpg".format(index=i),image)
    sleep(0.15)
    result = _model.predict_from_file("capture_"+str(i)+".jpg")
    print("Your choice is {choice}".format(choice=result.prediction))
    
    HAT.set_pixels(value)
    sleep(0.50)
    _didYouWin = didYouWin(result.prediction, key)

    if _didYouWin == 1:
      HAT.set_pixels(win)
    elif _didYouWin == 0:
      HAT.set_pixels(lose)
    else:
      HAT.clear()
    sleep(0.50)

def didYouWin(_yourChoice, _PIChoice):
  if _yourChoice == "scissors" and _PIChoice == "paper":
    return 1
  elif _yourChoice == "rock" and _PIChoice == "scissors":
    return 1
  elif _yourChoice == "paper" and _PIChoice == "rock":
    return 1
  elif _yourChoice == _PIChoice:
    return -1
  else:
    return 0

def main():
  HAT.clear()
  print("Initializing, please wait...")
  model = ImageModel.load("model")
  print("Initializing is completed. Press the button to start...")
  while True:
    for event in HAT.stick.get_events():
      if event.action == "pressed":
        if event.direction == "middle":
          print('Let\'s play Rock-Scissors-Paper')
          playRockSciccorsPaper(3,model)
          HAT.clear()
          print('This round is completed. Press button to play again.')
        else:
          print("Terminating application, please wait...")
          sys.exit(0)




if __name__ == "__main__":
    main()