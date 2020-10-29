from PIL import ImageGrab
from win32 import win32clipboard
import time
import msvcrt
name=time.time()

name=(str(name))


im = ImageGrab.grabclipboard()   # this is the part that grabs the image from the clipboard
print('do you wish to save all images from the clip board as png files :')
print('\npress 1+enter for yes')
print('press enter to continue without saving \n \t\t___',end="\b\b")
n=input()


if n==1:
    n=True
try:
    im.show()
    
except:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    print("this text was previously copied to the clipboard not an image :\n---------------------------------------------------------------------------------------- \n",data)
    print("\n----------------------------------------------------------------------------------------")
    win32clipboard.CloseClipboard()
else:

    print("\n\n the image has been saved with the name {}.png ".format(name))
    im.save(name+'.png','PNG')
    im.close()

print("\n\n  press enter to exit...")
msvcrt.getch()
