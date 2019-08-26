import pymysql
import os
# import demo1
import PIL.Image as Image

import math

orgDb="wuzhen_item_pic"
targetDb="wuzhen_target_pic"
orgSize=6000
targetSize=277


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
    sql = "UPDATE %s SET target_imgs = '%s' WHERE id = '%d'" % (orgDb,url,s_id)
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
    sql = "UPDATE %s SET is_use = 1 WHERE id = '%d'" % (targetDb,al_id)
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

    for index in range(start,targetSize+1,2):
        all_shen = formatSqlImg(targetDb,index)
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


for index in range(1,orgSize+1):
    shen = formatSqlImg(orgDb,index)
    ids = shen[0][0]
    r = shen[0][3]
    g = shen[0][4]
    b = shen[0][5]
    resf(ids,r,g,b)
    print("完成 %.2f" %((index/orgSize)*100)+"%")