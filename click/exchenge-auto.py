import time
from time import sleep

import pyautogui
import mouse
import winsound
import keyboard

# 795.14
# проверка загрузки
def check(pause):
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((795, 14))
    print(f"цвет {pixel_color}")
    while pixel_color != (195, 220, 253):
        time.sleep(pause)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((795, 14))
        mouse.move(1000, 1000)
        print(f"цвет {pixel_color}")

def expectation():
    time.sleep(pause)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1830, 150))
    # print(f"цвет {pixel_color}")
    while pixel_color != (175, 199, 101):
        time.sleep(pause + 2)
        mouse.move(700, 1070)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((1830, 150))
        #print(f"цвет {pixel_color}")
        if keyboard.press("backspace"):
            break
        time.sleep(pause)
    if pixel_color == (175, 199, 101):
        winsound.PlaySound("brosok-odnoy-monetki-v-obschuyu-kuchu.wav", winsound.SND_ALIAS)
        winsound.PlaySound(
            "zvuk-monetyi-na-tverdoy-poverhnosti-4-30628.wav",
            winsound.SND_ALIAS)
        time.sleep(pause)
    time.sleep(pause)

# конвертация usdt в avax
def conv_usdt_avax(pause):
    time.sleep(1)
    mouse.move(600, 160)
    mouse.click()
    time.sleep(5)

    check(pause)

    mouse.move(1030, 430)
    mouse.click()
    time.sleep(pause)

    keyboard.send('u')
    time.sleep(pause)

    #mouse.move(1030, 560)
    #mouse.click()
    #time.sleep(pause)

    mouse.move(1800, 430)
    mouse.click()
    time.sleep(pause)

    mouse.move(1800, 530)
    time.sleep(pause)
    mouse.wheel(-3)
    time.sleep(pause)

    mouse.move(1800, 990)
    time.sleep(pause)
    mouse.click()
    time.sleep(pause)

    mouse.move(470, 420)
    mouse.click()
    time.sleep(pause)
    for i in range(4):
        keyboard.send('backspace')
    keyboard.send('5')
    keyboard.send('0')
    keyboard.send('0')
    time.sleep(pause)

    mouse.move(1800, 540)
    mouse.click()
    time.sleep(2)

    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1820, 170))
    #print(f"цвет {pixel_color}")
    while pixel_color != (20, 20, 22):
        winsound.PlaySound("d0ceb42813793b7.mp3", winsound.SND_ALIAS)
        time.sleep(5)
        mouse.move(1800, 540)
        mouse.click()
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((1820, 170))
        #print(f"цвет {pixel_color}")
    time.sleep(3)

# трансфер avax
def trans_avax_spot(pause):
    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    check(pause)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
    60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)

    mouse.move(380, 250)
    mouse.click()
    time.sleep(pause)



    # 870 390
    # 1040 810

    mouse.move(870, 390)
    mouse.click()
    time.sleep(pause)

    keyboard.send('a')
    time.sleep(pause)
    keyboard.send('v')
    time.sleep(pause)

    mouse.move(870, 390)
    mouse.click()
    time.sleep(pause)

    #mouse.move(870, 500)
    #time.sleep(pause)
    #mouse.wheel(-3)
    #time.sleep(pause)
#
    #mouse.move(870, 870)
    #mouse.click()
    #time.sleep(pause)

    mouse.move(1040, 810)
    mouse.click()
    time.sleep(pause)

    mouse.move(870, 890)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)
    #print(f"цвет {pixel_color}")
    #print(f"цвет {pixel_cont}")

def sell_avax(pause):
    #mouse.move(400, 160)
    #mouse.click()
    #time.sleep(1)
#
    ## 794 19
#
    #time.sleep(5)
    #screenshot = pyautogui.screenshot()
    #pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    #screenshot = pyautogui.screenshot()
    #pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    #while pixel_color == (23, 24, 27) and pixel_cont != (
    #60, 60, 60):
    #    winsound.PlaySound("*", winsound.SND_ALIAS)
    #    time.sleep(1)
    #    screenshot = pyautogui.screenshot()
    #    pixel_color = screenshot.getpixel((21, 324))
    #    print(f"цвет {pixel_color}")
    #    screenshot = pyautogui.screenshot()
    #    pixel_cont = screenshot.getpixel((797, 14))
    #    print(f"цвет {pixel_cont}")
    #time.sleep(3)

    check(pause)

    mouse.move(1630, 340)
    mouse.click()
    time.sleep(pause)

    keyboard.send('a')
    keyboard.send('v')
    time.sleep(pause)

    mouse.move(1630, 430)
    mouse.click()
    time.sleep(1)

    check(pause)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
    60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)

    mouse.move(1600, 900)
    time.sleep(pause)
    mouse.wheel(-4)
    time.sleep(pause)

    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1280, 750))
    #print(f"цвет {pixel_color}")
    if pixel_color != (255, 104, 56):
        mouse.wheel(10)
        time.sleep(1)

        mouse.move(400, 160)
        mouse.click()
        time.sleep(1)

        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
        while pixel_color == (
        23, 24, 27) and pixel_cont != (
                60, 60, 60):
            winsound.PlaySound("*", winsound.SND_ALIAS)
            time.sleep(1)
            screenshot = pyautogui.screenshot()
            pixel_color = screenshot.getpixel((21, 324))
            #print(f"цвет {pixel_color}")
            screenshot = pyautogui.screenshot()
            pixel_cont = screenshot.getpixel((797, 14))
            #print(f"цвет {pixel_cont}")
        time.sleep(1)

        mouse.move(1630, 340)
        mouse.click()
        time.sleep(1)

        keyboard.send('a')
        keyboard.send('v')
        time.sleep(1)

        mouse.move(1630, 430)
        mouse.click()
        time.sleep(1)

        time.sleep(5)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
        while pixel_color == (
        23, 24, 27) and pixel_cont != (
                60, 60, 60):
            winsound.PlaySound("*", winsound.SND_ALIAS)
            time.sleep(1)
            screenshot = pyautogui.screenshot()
            pixel_color = screenshot.getpixel((21, 324))
            #print(f"цвет {pixel_color}")
            screenshot = pyautogui.screenshot()
            pixel_cont = screenshot.getpixel((797, 14))
            #print(f"цвет {pixel_cont}")
        time.sleep(1)

        mouse.move(1600, 900)
        time.sleep(0.5)
        mouse.wheel(-4)
        time.sleep(1)

    mouse.move(1540, 635)
    mouse.click()
    time.sleep(1)

    mouse.move(1280, 750)
    mouse.click()
    time.sleep(pause)

    expectation()

    mouse.move(20, 200)
    time.sleep(pause)
    mouse.wheel(10)
    time.sleep(pause)

def trans_bnb_balance(pause):
    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    check(pause)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)
    #print(f"цвет {pixel_color}")
    #print(f"цвет {pixel_cont}")

    mouse.move(380, 250)
    mouse.click()
    time.sleep(pause)

    mouse.move(870, 390)
    mouse.click()
    time.sleep(pause)

    mouse.move(770, 530)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 500)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 560)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 600)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 640)
    mouse.click()
    time.sleep(pause)

    mouse.move(1050, 810)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 890)
    mouse.click()
    time.sleep(3)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)
    #print(f"цвет {pixel_color}")
    #print(f"цвет {pixel_cont}")

def conv_bnb_btc(pause):
    mouse.move(600, 160)
    mouse.click()
    time.sleep(5)

    check(pause)

    mouse.move(990, 430)
    mouse.click()
    time.sleep(pause)

    mouse.move(990, 615)
    mouse.click()
    time.sleep(pause)

    mouse.move(1800, 430)
    mouse.click()
    time.sleep(pause)

    mouse.move(1800, 500)
    mouse.click()
    time.sleep(pause)

    mouse.move(1070, 385)
    mouse.click()
    time.sleep(pause)

    mouse.move(1800, 540)
    mouse.click()
    time.sleep(2)

    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1820, 170))
    #print(f"цвет {pixel_color}")
    while pixel_color != (20, 20, 22):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(60)
        mouse.move(1800, 540)
        mouse.click()
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((1820, 170))
        #print(f"цвет {pixel_color}")
    time.sleep(5)

def trans_btc_spot(pause):
    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    check(pause)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)

    mouse.move(380, 250)
    mouse.click()
    time.sleep(pause)

    mouse.move(1050, 810)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 890)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)
    #print(f"цвет {pixel_color}")
    #print(f"цвет {pixel_cont}")

def sell_btc(pause):
    check(pause)

    time.sleep(3)
    mouse.wheel(-4)
    time.sleep(pause)

    mouse.move(1540, 635)
    mouse.click()
    time.sleep(pause)

    mouse.move(1280, 750)
    mouse.click()
    time.sleep(pause)

    expectation()

def trans_usdt_balance(pause):
    time.sleep(3)
    mouse.move(50, 200)
    time.sleep(pause)
    mouse.wheel(10)
    time.sleep(pause)

    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    check(pause)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
    60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)
    #print(f"цвет {pixel_color}")
    #print(f"цвет {pixel_cont}")

    mouse.move(380, 250)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 390)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 480)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 500)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 560)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 600)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 640)
    mouse.click()
    time.sleep(pause)

    mouse.move(1050, 810)
    mouse.click()
    time.sleep(pause)

    mouse.move(800, 890)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    #print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    #print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        #print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        #print(f"цвет {pixel_cont}")
    time.sleep(1)
    #print(f"цвет {pixel_color}")
    #print(f"цвет {pixel_cont}")

if __name__ == '__main__':
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((1802, 1068))
    print(f"цвет {pixel_cont}")
    if pixel_cont == (29, 29, 29):
        keyboard.send('shift + alt')
    pause = 0.5
    while True:
        conv_usdt_avax(pause)
        trans_avax_spot(pause)
        #conv_usdt_avax(pause)
        #trans_avax_spot(pause)
        #conv_usdt_avax(pause)
        #trans_avax_spot(pause)
        sell_avax(pause)
        trans_bnb_balance(pause)
        conv_bnb_btc(pause)
        trans_btc_spot(pause)
        sell_btc(pause)
        trans_usdt_balance(pause)
        check(pause)


