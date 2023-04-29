import pyautogui as pag
import pydirectinput as pdi
from time import sleep

left_right=0.2
up_down=1.7

for i in range(1,4):
    sleep(1)
    print(i)
    
pag.mouseDown()

while True:
    for i in range(1,5):
        pdi.keyDown('w')
        sleep(up_down)
        pdi.keyUp('w')

        pdi.keyDown('d')
        sleep(left_right)
        pdi.keyUp('d')

        pdi.keyDown('s')
        sleep(up_down)
        pdi.keyUp('s')

        pdi.keyDown('d')
        sleep(left_right)
        pdi.keyUp('d')
        
    for i in range(1,5):
        pdi.keyDown('w')
        sleep(up_down)

        pdi.keyUp('w')

        pdi.keyDown('a')
        sleep(left_right)
        pdi.keyUp('a')

        pdi.keyDown('s')
        sleep(up_down)
        pdi.keyUp('s')
        
        pdi.keyDown('a')
        sleep(left_right)
        pdi.keyUp('a')

