# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class GoodjobsPipeline(object):
    def __init__(self):
        #建立数据库连接
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='goodjobs',charset='utf8')
        #创建操作游标
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        #定义sql语句
        sql = "INSERT INTO `goodjobs`.`t_jobs` (`jobname`, `corpname`) VALUES ('"+item['jobname'][0]+"', '"+item['jobname'][1]+"');"

        #执行sql语句
        self.cursor.execute(sql)
        #保存修改
        self.connection.commit()

        return item

    def __del__(self):
        #关闭操作游标
        self.cursor.close()
        #关闭数据库连接
        self.connection.close()
