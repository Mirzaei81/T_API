from os import listdir
from table import P_name,session
from random import randrange
from PIL import Image,ImageDraw,ImageFont
colors = ["2044E8","17F105"]
files  = listdir("./images/")
x = files[randrange(len(files))]
names = session.query(P_name).all()

for name in names:
    if name.name == x:
        print(name.name ," : " , name.des)
        nm =  listdir(f'./images/{x}')
        f= Image.open(f"./images/{x}/{nm[0]}")
        font = int(f.size[0]/8)
        I_font = ImageFont.truetype("Cotton Butter.ttf",font)
        d = ImageDraw.Draw(f)
        w , h = d.textsize(x,font=I_font)
        d.text(((f.size[0]-w)/2,f.size[1]-(font*1)),x,fill=f"#{colors[randrange(len(colors))]}",font=I_font)
        f.save(f"modified/{x}.jpg")

