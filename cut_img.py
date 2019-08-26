from PIL import Image
import os

filePath = "pic7"
outPutPath = "pic8"

# paths = os.listdir(filePath)
# num = 0
# for path in paths:
#     num += 1
#     first_name, second_name = os.path.splitext(path)
#     files = os.path.join(filePath, path)
#     img = Image.open(files)
#     width = img.size[0]
#     height = img.size[1]
#     x0,y0,x1,y1 = 0,0,0,0
#     if width > height:
#         # 说明是横图
#         x0 = (width -height)/2
#         y0 = 0
#         x1 = x0+height
#         y1 = height
#     else:
#         x0 = 0
#         y0 = (height - width)/2
#         x1 = width
#         y1 = y0 + width
#     copyImg = img.crop((x0,y0,x1,y1))
#     # copyImg.show()
#     # outImg = copyImg.resize((256,256))
#     copyImg.save(outPutPath+str(num)+".bmp")

paths = os.listdir(filePath)
num = 0
for path in paths:
    # global num
    try:
        num += 1
        first_name, second_name = os.path.splitext(path)
        files1 = os.path.join(filePath, path)
        img = Image.open(files1)
        img = img.resize((256, 256),Image.ANTIALIAS)
        img.save(outPutPath+"/"+first_name+".jpg")  
    except:
        pass
    