import pyautogui as auto
import time

'''
training app for mac

0, 138, 204 => 開始行動
mouse position => 1598, 968

76, 10, 0 => 開始遊戲operation start
mouse position => 1598, 735

255, 150, 2 => 行動結束
mouse position => 1477, 789
'''

pixel = [
    { 'color': (0, 138, 204, 255), 'cord': (1598, 968) },
    { 'color': (76, 10, 0, 255), 'cord': (1598, 735) },
    { 'color': (255, 150, 2, 255), 'cord': (1477, 789) }
]


def click_given_element(pixel):
    image = auto.screenshot()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            found_pixel = image.getpixel((i, j))
            if found_pixel in [pixel[k]['color'] for k in range(len(pixel))]:
                print(f'pixel found! {found_pixel}')
                for l in range(len(pixel)):
                    if pixel[l]['color'] == found_pixel:
                        print(f'clicking on cords: {pixel[l]["cord"][0]}, {pixel[l]["cord"][1]}')
                        auto.click(pixel[l]['cord'][0], pixel[l]['cord'][1])
                        time.sleep(1)
                        return
    print('element not found, wait for next loop...')
    time.sleep(1)
    return


def main():
    while True:
        # check for existing elements
        # if found, click
        click_given_element(pixel=pixel)


if __name__ == '__main__':
    main()