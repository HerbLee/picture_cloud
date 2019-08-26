import pymysql
import os
import demo1
import PIL.Image as Image


def formatSql(img,r,g,b):

    db = pymysql.connect("localhost","root","sy!)#@#@","taobao_sy")
    cursor = db.cursor()
 
    # SQL 插入语句
    sql = "INSERT INTO wuzhen_item_pic(org_imgs, r_color, g_color, b_color) VALUES ('%s', '%d',  %d,  '%d')" %(img, r, g,b)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    
    # 关闭数据库连接
    db.close()

num = 0
num1 = 0
num2 = 0
totalNo = 6000

dir = 'pic7'
dirs = os.listdir(dir)
for dirc in dirs:
    file_dir = dir+"/"+dirc
    image = Image.open(file_dir)
    image = image.convert('RGB')
    imgg = demo1.get_dominant_color(image)
    try:
        formatSql(file_dir,imgg[0],imgg[1],imgg[2])
        num1 = num1+1
    except Exception as e:
        formatSql(file_dir,255,255,255)
        num2 = num2+1
    num = num+1
    print("完成 %.2f" %((num/totalNo)*100) +"%")

print("正常: %d 错误: %d 总:%d" %(num1,num2,num))