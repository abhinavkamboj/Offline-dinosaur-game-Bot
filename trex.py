import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui

mon = {'top': 418, 'left': 180, 'width': 75, 'height': 35}#area of interest on the screen

k=1
while 1:
    img=mss().grab(mon) #get raw pixels from the screen
    img=np.array(img)   # Get raw pixels from the screen, save it to a Numpy array
    
    cv2.imshow('test', img) #just displaying the image
    p_cactus =img[28,:,0]     #storing the blue colour's value of all pixels from 28th pixel 
    p_bird =img[1,:,0]     # storing the blue colour's value of all pixels from 1st pixel
    
    p_cactus_sum=np.sum(p_cactus)  #sum of all the blue values at 28th position
    p_bird_sum=np.sum(p_bird)
    print (p_cactus_sum)
    #print (p_bird_sum)
    

    if p_cactus_sum<18525:
     pyautogui.press('up')
    
    if p_bird_sum<18525:
     pyautogui.keyDown('down')
     print (p_bird_sum)
     k=1     
    
    if p_bird_sum==18525 and k==1:
           pyautogui.keyUp('down')
           k=0
    #if cv2.waitKey(25) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
        #break
