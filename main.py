import mss
import numpy as np
import pyautogui
import time
import cv2
import webbrowser
from tkinter import *

def screen_record_efficient():
   mon={"top":215,"left":315,"width":100,"height":100}
   title="[MSS] fps benchmark"
   fps = 0
   rib=0
   sct = mss.mss()
   last_time = time.time()
   hook = True
   while True:
      img = np.asarray(sct.grab(mon))
      fps+=1  
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      lower_red = np.array([0, 50, 50])
      upper_red = np.array([10, 255, 255])
      mask0 = cv2.inRange(hsv, lower_red, upper_red)     
      lower_red = np.array([170, 50, 50])
      upper_red = np.array([180, 255, 255])
      mask1 = cv2.inRange(hsv, lower_red, upper_red)     
      mask = mask0 + mask1 
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
   window.destroy()
   return fps
def exit1():
    exit(0)
def vk():
   webbrowser.open('https://vk.com/gn1dor', new=2)
def tg():
   webbrowser.open('https://t.me/gn1dor', new=2)

window = Tk()
window.title("Bots by gn1dor")
window.geometry('350x300')
window.resizable(width=False,height=False)
window['background']='#856ff8'
lbl = Label(window, text="Данная программа была сделанна на голом энтузиазме.").pack(side=TOP)
lbl1= Label(window,text="Программа абсолютно бесплатна,в случае если вы ").pack(side=TOP)
lbl2= Label(window,text="хотите поддержать проект напишите разработчику").pack(side=TOP)
lbl4= Label(window,text="!!!Обязательно прочитайте файл :Прочитай меня!!!").pack(side=TOP)
lbl5= Label(window,text="!!!Be sure to read the file:README!!!").pack(side=TOP)
lbl3= Label(window,text="Контакты:").pack(side=RIGHT)
btn3 = Button(window, text="vk", command=vk).pack(side=RIGHT)
btn4 = Button(window, text="tg", command=tg).pack(side=RIGHT)
btn1 = Button(window, text="начать рыбалку", command=screen_record_efficient).pack(side=BOTTOM)
btn2 = Button(window, text="закончить рыбалку", command=window.destroy).pack(side=BOTTOM)
window.mainloop()




