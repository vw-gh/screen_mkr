import pyscreenshot
from PIL import ImageGrab
import os
from datetime import datetime

# разрешение экрана
width, height = ImageGrab.grab().size

img = pyscreenshot.grab(bbox=(0, 0, width, height))

#do & show img
# img.show()

dt = datetime.now().strftime('%m_%d-%H_%M_%S')
img.save(dt + '.png')


# print(os.getcwd())