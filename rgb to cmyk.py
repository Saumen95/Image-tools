import numpy as np
from PIL import Image
import pyhdust as hdt
import pyhdust.images as phim

# RGB to CMYK
img = 'Flag_of_Brazil.png'
img = Image.open(img)
img = img.convert(mode='RGB')
img = phim.rgb2cmyk(np.asarray(img))
img = Image.fromarray(img, mode='CMYK')
img.save('FlagCYMK.jpg')

# CMYK to RGB: PIL way
img = hdt.hdtpath()+'pyhdust/refs/repo/CMYK2rgb.jpg'
img = Image.open(img)
img.save('cmyk.jpg')
# img.save('rgb.jpg', mode='RGB') Does not work!
img = img.convert(mode='RGB')
img.save('rgb.jpg')
