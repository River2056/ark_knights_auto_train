import pyautogui as auto
import time

'''
    training app for windows
'''
# mission_tag = auto.locateOnScreen('OFF4.png')
# print(mission_tag)

# start_tag = auto.locateOnScreen('start.png')
# print(start_tag)

# commence_btn = auto.locateOnScreen('commence.png')
# success_tag = auto.locateOnScreen('success.png')
# print(success_tag)


def click_on_element(tag):
    tag_x, tag_y = auto.center(tag)
    auto.click(tag_x, tag_y)
    time.sleep(1)


counter = 1
while counter > 0:
    counter -= 1
    print(f'auto train commence in {counter} seconds...')
    
    start_tag = auto.locateOnScreen('start_36.png')
    # start_tag = auto.locateOnScreen('start_18.png')
    commence_btn = auto.locateOnScreen('commence.png')
    success_tag = auto.locateOnScreen('success.png')
    print(start_tag)
    print(commence_btn)
    print(success_tag)

    if counter == 0:
        if start_tag != None:
            click_on_element(start_tag)
            counter = 1
        elif commence_btn != None:
            click_on_element(commence_btn)
            counter = 1
        elif success_tag != None:
            click_on_element(success_tag)
            counter = 1
        else:
            print('training in progress, or button not found')
            counter = 1

    time.sleep(1)
