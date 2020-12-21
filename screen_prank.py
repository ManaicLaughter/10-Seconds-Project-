import rotatescreen
import time
screen = rotatescreen.get_primary_display()

#you can change time and range from 13 to 1000 to 100000000....to make it look more crazy.
for i in range(13):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)
