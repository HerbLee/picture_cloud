import PIL.Image as Image
import os
import pymysql
#  pic1/
IMAGES_PATH = ''  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = 256  # 每张小图片的大小
IMAGE_ROW = 100  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 60  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = 'slqq.jpg'  # 图片转换后的地址
 

image_names = []
# # dir = 'D://pics/沈月'
# # dirs = os.listdir(dir)
# # for dirc in dirs:
# #     files = os.listdir(dir+"/"+dirc)
# #     for file in files:
# #         image_names.append(dir+"/"+dirc+"/"+file)

#         # print(dir+"/"+dirc+"/"+file)


# def formatSqlImg(name1):
#     print(name1)
#     db = pymysql.connect("localhost","root","sy!)#@#@","taobao_sy")
#     cursor = db.cursor()
    
#     imgs = ""
    
#     # SQL 插入语句
#     sql = "SELECT * FROM nezha_item_pic where org_imgs='%s'" %(name1)
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         results = cursor.fetchall()
    
#         imgs = results[0][2]
#         # print(results[0][1])
#         # for row in results:
#         #     print(row)
#         #     imgs.append(row)
#     except Exception as e:
#         print("运行")
#         print(e)
#         # 发生错误时回滚
#         db.rollback()
    
#     # 关闭数据库连接
#     db.close()
#     return imgs

for index in range(1,6001):
    img = "pic9/"+str(index)+".jpg"
    image_names.append(img)
    progress = index*100/6001
    print("完成 %s "%(str(progress)))
# index=1
# img = formatSqlImg(str(index)+".jpg")
# 获取图片集地址下的所有图片名称
# image_names = [str(name)+".jpg" for name in range(1,577)]


 
# # 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")
 
# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
            progress = ((y-1)*IMAGE_ROW + x)*100/1500
            print("完成 %s " %(progress))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图

image_compose() #调用函数

