import pymysql
import os
# import demo1
import PIL.Image as Image

import math


def formatSqlImg(table,ids):

    db = pymysql.connect("localhost","root","sy!)#@#@","taobao_sy")
    cursor = db.cursor()
    
    imgs = []

    # SQL 插入语句
    sql = "SELECT * FROM %s where id=%d" %(table,ids)
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            # print(row)
            imgs.append(row)
    except:
        # 发生错误时回滚
        db.rollback()
    
    # 关闭数据库连接
    db.close()
    return imgs

def sqlsIns(s_id,url):
    db = pymysql.connect("localhost","root","sy!)#@#@","taobao_sy")
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = "UPDATE nezha_item_pic SET target_imgs = '%s' WHERE id = '%d'" % (url,s_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
 
    # 关闭数据库连接
    db.close()


def ssq(al_id):
    db = pymysql.connect("localhost","root","sy!)#@#@","taobao_sy")
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = "UPDATE nezha_target_pic SET is_use = 1 WHERE id = '%d'" % (al_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
 
    # 关闭数据库连接
    db.close()


def resf(id,r,g,b):
    nos = 1000
    arr = ""
    start = (id%2)+1

    for index in range(start,91,2):
        all_shen = formatSqlImg("nezha_target_pic",index)
        is_use = all_shen[0][5]
        id1 = all_shen[0][0]
        r1 = all_shen[0][2]
        g1 = all_shen[0][3]
        b1 = all_shen[0][4]

        num = math.sqrt((r-r1)**2 +(g-g1)**2 +(b-b1)**2)
        if num < nos:
            nos = num
            arr = all_shen[0]
    
    # print(arr)
    sqlsIns(id,arr[1])
    ssq(arr[0])


for index in range(1,1501):
    shen = formatSqlImg("nezha_item_pic",index)
    ids = shen[0][0]
    r = shen[0][3]
    g = shen[0][4]
    b = shen[0][5]
    resf(ids,r,g,b)
    print("完成 %.2f" %((index/1500)*100)+"%")

# all_shen = formatSqlImg("all_shenyue",1)


# print(all_shen)