import pyscreenshot
from PIL import ImageGrab

# разрешение экрана
width, height = ImageGrab.grab().size

img = pyscreenshot.grab(bbox=(0, 0, width, height))

img.show()