import pyautogui as pg 
from time import sleep
import webbrowser
import os 
##

pg.FAILSAFE = True

screen_size = list(pg.size())

webbrowser.open('https://google.com')

sleep(5)

x, y = list(pg.locateCenterOnScreen(r"c:\Users\User\Videos\Desktop\Desktop Screenshot 2023.01.21 - 15.55.47.31_2.png"))

pg.moveTo(x, y)

pg.click()

pg.typewrite("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley", interval=0.001)

pg.press('enter')

sleep(2)

x, y  = list(pg.locateCenterOnScreen('preview.png'))

pg.moveTo(x, y)

pg.click()

sleep(3)

x, y = list(pg.locateCenterOnScreen('full_screen.png'))

pg.moveTo(x, y)

pg.click()

for i in range(100):

    pg.alert(text='You\'ve been rickroled! 😎')