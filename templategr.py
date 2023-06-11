import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
# Import some shit I need to use

# Initializate lists
posX = list()
posY = list()

# Bad at math
for x in range(20):
    if(x<10):
        if((x%2)==0):
            posX.append(0)
        else:
            posX.append(160)
    else:
        if((x%2)==0):
            posX.append(1620)
        else:
            posX.append(1780)

# True crime here
for n in range(2):       
    for y in range(5):
        posY.append(80 + y*180)
        posY.append(80 + y*180)

#
#posX = posX [:20]
#posY = posY [:20]


if(len(posX)>20):
    print("Muito grande")

template = Image.open("template.png")
ruuka = Image.open("ruuka.png").resize((140,140), Image.LANCZOS)

draw = ImageDraw.Draw(template)
font = ImageFont.truetype("arial.ttf", size=60)
na = 0
for x2 in posX:
            y2 = posY[na]
            template.paste (ruuka, (x2, y2))
            draw.text((x2+70, y2+135), str(na+1), font=font, fill='black', anchor='ms')
            na+=1

print(len(posX))
print(len(posY))
# template.paste (ruuka, (0, 80))
print(template)
template = template.save("sexo.png")
