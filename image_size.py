print('Hi')

from PIL import Image
import os
# 給定對照圖片
img1 = Image.open('./assets/img/latest-news/TMU_school.jpg')
# cchange image  size
img2 = Image.open('./assets/img/latest-news/NDMC_school.jpg')

img2 = img2.resize(img1.size)

img2.save('./assets/img/latest-news/NDMC_school.jpg')