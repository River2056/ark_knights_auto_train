import pyautogui as auto

pixel = [
    { 'color': (0, 138, 204, 255), 'cord': (1598, 968) },
    { 'color': (76, 10, 0, 255), 'cord': (1598, 735) },
    { 'color': (255, 150, 2, 255), 'cord': (1477, 789) }
]
# print(pixel.count((0, 138, 204)))

image = auto.screenshot()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        if image.getpixel((i, j)) in [pixel[k]['color'] for k in range(len(pixel))]:
            print(f'found pixel! {image.getpixel((i, j))}')
            for l in range(len(pixel)):
                if pixel[l]['color'] == image.getpixel((i, j)):
                    print(f'clicking on element {pixel[l]["cord"]}')
