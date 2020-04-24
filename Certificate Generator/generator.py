import pandas as pd 
from PIL import Image, ImageDraw, ImageFont


# reading csv file 
data = pd.read_csv("Book1.csv")

name = data.iloc[:,0].values
position = data.iloc[:,1].values
#print(name)
#print(position)

fnt1 = ImageFont.truetype('futura_medium_bt.ttf', 90)
fnt2 = ImageFont.truetype('futura_medium_bt.ttf', 75)

#img = Image.open('Cert.png')
#d = ImageDraw.Draw(img)

for i in range(0, len(name)):
    img = Image.open('Cert.png')
    d = ImageDraw.Draw(img)
    d.text((1400,910), text = name[i], fill = (0, 0, 0), font = fnt1)
    d.text((1320,1200), text = position[i], fill = (0, 0, 0), font = fnt2)
    img.save(name[i]+'.png')
  

