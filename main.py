import mss
import numpy as np
import pyautogui
import time
import cv2

def screen_record_efficient():
   mon={"top":215,"left":315,"width":100,"height":100}
   title="[MSS] fps benchmark"
   fps = 0
   rib=0
   sct = mss.mss()
   last_time = time.time()
   hook = True
   print("RU ____ Данная программа была сделанна на голом энтузиазме. Актуальные контакты для связи: https://vk.com/gn1dor  viktnnchik#9558 программа абсолютно бесплатна,в случае если вы хотите поддержать проект напишите разработчику"
        "EN ____ This program was made on bare stream. Actual contacts for communication: https://vk.com/gn1dor viktnnchik#9558 the program is absolutely free, if you want to support the project write to the developer")



   while True:

      img = np.asarray(sct.grab(mon))
      fps+=1

      # create hsv
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

      # define masks
      # lower mask (0-10)
      lower_red = np.array([0, 50, 50])
      upper_red = np.array([10, 255, 255])
      mask0 = cv2.inRange(hsv, lower_red, upper_red)

      # upper mask (170-180)
      lower_red = np.array([170, 50, 50])
      upper_red = np.array([180, 255, 255])
      mask1 = cv2.inRange(hsv, lower_red, upper_red)

      # join masks
      mask = mask0 + mask1

      # check
      hasRed = np.sum(mask)
      if hasRed > 0:

         time.sleep(0.25)
      else:

         pyautogui.click()
         time.sleep(0.25)



      cv2.imshow(title,img)

      if cv2.waitKey(25) & 0xFF == ord("q"):
         cv2.destroyAllWindows()
         break

   return fps



print("MSS:",screen_record_efficient())


