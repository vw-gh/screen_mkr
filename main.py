import pyscreenshot
import win32api
import screeninfo
from PIL import ImageGrab


print(screeninfo.get_monitors())

img = ImageGrab.grab()
print (img.size)
img = pyscreenshot.grab(bbox=(10, 10, 1920, 510))

img.show()

# img.save('myimg2.png')

