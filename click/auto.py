import time
import pyautogui
import mouse
import winsound
import keyboard


def expectation():
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1830, 150))
    # print(f"цвет {pixel_color}")
    time.sleep(0.1)
    while pixel_color != (175, 199, 101):
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((1830, 150))
        #print(f"цвет {pixel_color}")
        time.sleep(0.1)
    if pixel_color == (175, 199, 101):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(0.5)
    time.sleep(2)

# конвертация usdt в avax
def conv_usdt_avax():
    time.sleep(1)
    mouse.move(600, 160)
    mouse.click('left')
    time.sleep(5)
    mouse.move(1030, 430)
    mouse.click('left')
    time.sleep(1)
    mouse.move(1030, 560)
    mouse.click('left')
    time.sleep(1)
    mouse.move(1800, 430)
    mouse.click('left')
    time.sleep(1)
    mouse.move(1800, 530)
    time.sleep(1)
    mouse.wheel(-3)
    time.sleep(1)
    mouse.move(1800, 990)
    time.sleep(1)
    mouse.click('left')
    time.sleep(1)

    mouse.move(470, 420)
    mouse.click('left')
    time.sleep(1)
    for i in range(4):
        keyboard.send('backspace')
        time.sleep(0.2)
    keyboard.send('5')
    keyboard.send('0')
    keyboard.send('0')
    time.sleep(1)

    mouse.move(1800, 540)
    mouse.click()
    time.sleep(2)

    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1820, 170))
    print(f"цвет {pixel_color}")
    while pixel_color != (20, 20, 22):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(60)
        mouse.move(1800, 540)
        mouse.click()
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((1820, 170))
        print(f"цвет {pixel_color}")
    time.sleep(5)

# трансфер avax
def trans_avax_spot():
    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
    60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)

    mouse.move(380, 250)
    mouse.click()
    time.sleep(1)

    # 870 390
    # 1040 810

    mouse.move(870, 390)
    mouse.click()
    time.sleep(1)

    mouse.move(870, 500)
    time.sleep(0.5)
    mouse.wheel(-3)
    time.sleep(0.5)

    mouse.move(870, 870)
    mouse.click()
    time.sleep(1)

    mouse.move(1040, 810)
    mouse.click()
    time.sleep(1)

    mouse.move(870, 890)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)
    print(f"цвет {pixel_color}")
    print(f"цвет {pixel_cont}")

def sell_avax():
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
    time.sleep(3)

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
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
    60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)

    mouse.move(1600, 900)
    time.sleep(0.5)
    mouse.wheel(-4)
    time.sleep(1)

    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1280, 750))
    print(f"цвет {pixel_color}")
    if pixel_color != (255, 104, 56):
        mouse.wheel(10)
        time.sleep(1)

        mouse.move(400, 160)
        mouse.click()
        time.sleep(1)

        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
        while pixel_color == (
        23, 24, 27) and pixel_cont != (
                60, 60, 60):
            winsound.PlaySound("*", winsound.SND_ALIAS)
            time.sleep(1)
            screenshot = pyautogui.screenshot()
            pixel_color = screenshot.getpixel((21, 324))
            print(f"цвет {pixel_color}")
            screenshot = pyautogui.screenshot()
            pixel_cont = screenshot.getpixel((797, 14))
            print(f"цвет {pixel_cont}")
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
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
        while pixel_color == (
        23, 24, 27) and pixel_cont != (
                60, 60, 60):
            winsound.PlaySound("*", winsound.SND_ALIAS)
            time.sleep(1)
            screenshot = pyautogui.screenshot()
            pixel_color = screenshot.getpixel((21, 324))
            print(f"цвет {pixel_color}")
            screenshot = pyautogui.screenshot()
            pixel_cont = screenshot.getpixel((797, 14))
            print(f"цвет {pixel_cont}")
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
    time.sleep(1)

    expectation()

    mouse.move(20, 200)
    time.sleep(1)
    mouse.wheel(10)
    time.sleep(1)

def trans_bnb_balance():
    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)
    print(f"цвет {pixel_color}")
    print(f"цвет {pixel_cont}")

    mouse.move(380, 250)
    mouse.click()
    time.sleep(1)

    mouse.move(870, 390)
    mouse.click()
    time.sleep(1)

    mouse.move(770, 530)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 500)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 560)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 600)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 640)
    mouse.click()
    time.sleep(1)

    mouse.move(1050, 810)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 890)
    mouse.click()
    time.sleep(3)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)
    print(f"цвет {pixel_color}")
    print(f"цвет {pixel_cont}")

def conv_bnb_btc():
    mouse.move(600, 160)
    mouse.click()
    time.sleep(5)

    mouse.move(990, 430)
    mouse.click()
    time.sleep(1)

    mouse.move(990, 615)
    mouse.click()
    time.sleep(1)

    mouse.move(1800, 430)
    mouse.click()
    time.sleep(1)

    mouse.move(1800, 500)
    mouse.click()
    time.sleep(1)

    mouse.move(1070, 385)
    mouse.click()
    time.sleep(1)

    mouse.move(1800, 540)
    mouse.click()
    time.sleep(2)

    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((1820, 170))
    print(f"цвет {pixel_color}")
    while pixel_color != (20, 20, 22):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(60)
        mouse.move(1800, 540)
        mouse.click()
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((1820, 170))
        print(f"цвет {pixel_color}")
    time.sleep(5)

def trans_btc_spot():
    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)

    mouse.move(380, 250)
    mouse.click()
    time.sleep(1)

    mouse.move(1050, 810)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 890)
    mouse.click()
    time.sleep(3)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)
    print(f"цвет {pixel_color}")
    print(f"цвет {pixel_cont}")

def sell_btc():
    time.sleep(3)
    mouse.wheel(-4)
    time.sleep(1)

    mouse.move(1540, 635)
    mouse.click()
    time.sleep(1)

    mouse.move(1280, 750)
    mouse.click()
    time.sleep(1)

    expectation()

def trans_usdt_balance():
    time.sleep(3)
    mouse.move(50, 200)
    time.sleep(1)
    mouse.wheel(10)
    time.sleep(1)

    mouse.move(400, 160)
    mouse.click()
    time.sleep(1)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
    60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)
    print(f"цвет {pixel_color}")
    print(f"цвет {pixel_cont}")

    mouse.move(380, 250)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 390)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 480)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 500)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 560)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 600)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 640)
    mouse.click()
    time.sleep(1)

    mouse.move(1050, 810)
    mouse.click()
    time.sleep(1)

    mouse.move(800, 890)
    mouse.click()
    time.sleep(3)

    time.sleep(5)
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((21, 324))
    print(f"цвет {pixel_color}")
    screenshot = pyautogui.screenshot()
    pixel_cont = screenshot.getpixel((797, 14))
    print(f"цвет {pixel_cont}")
    while pixel_color == (23, 24, 27) and pixel_cont != (
            60, 60, 60):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        pixel_color = screenshot.getpixel((21, 324))
        print(f"цвет {pixel_color}")
        screenshot = pyautogui.screenshot()
        pixel_cont = screenshot.getpixel((797, 14))
        print(f"цвет {pixel_cont}")
    time.sleep(1)
    print(f"цвет {pixel_color}")
    print(f"цвет {pixel_cont}")

if __name__ == '__main__':
    while True:
        conv_usdt_avax()
        trans_avax_spot()
        #conv_usdt_avax()
        #trans_avax_spot()
        #conv_usdt_avax()
        #trans_avax_spot()
        sell_avax()
        trans_bnb_balance()
        conv_bnb_btc()
        trans_btc_spot()
        sell_btc()
        trans_usdt_balance()

    #screenshot = pyautogui.screenshot()
    #pixel_color = screenshot.getpixel((1150, 560))
    #print(f"цвет {pixel_color}")

#screenshot = pyautogui.screenshot()
#pixel_color = screenshot.getpixel((21, 324))
#print(f"цвет {pixel_color}")
#while True:
#    screenshot = pyautogui.screenshot()
#    pixel_color = screenshot.getpixel((21, 324))
#    if pixel_color == (107, 126, 145):
#        print("цвет")
#    if pixel_color != (107, 126, 145):
#        print("цвета нет")



#pyautogui.moveTo(400, 160)
#pyautogui.click()
#screenshot = pyautogui.screenshot()
#pixel_color = screenshot.getpixel((21, 322))
#time.sleep(10)
#pyautogui.moveTo(370, 250)
#pyautogui.click()
#time.sleep(1)
#print(f"цвет {pixel_color}")
#pyautogui.moveTo(800, 380)
#pyautogui.click()
#pyautogui.moveTo(800, 440)
#time.sleep(1)
#mouse.wheel(-3)
#time.sleep(0.5)
#mouse.move(800, 870)
#mouse.click('left')
#time.sleep(0.5)
#mouse.move(1050, 810)
#mouse.click('left')
#time.sleep(0.5)
#mouse.move(900, 880)
#mouse.click('left')
#time.sleep(0.5)