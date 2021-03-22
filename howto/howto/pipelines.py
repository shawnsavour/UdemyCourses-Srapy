# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql

class HowtoPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_database()
        self.create_table()

    def create_connection(self):
        self.mydb = pymysql.connect(
        host="localhost",
        user="root",
        password=""
        )
        self.mycursor = self.mydb.cursor()

    def create_database(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS getudemy")

    def create_table(self):
        self.mycursor.execute("USE getudemy")
        self.mycursor.execute("DROP TABLE courses")
        createtable = '''CREATE TABLE IF NOT EXISTS courses (id integer NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                                    course MEDIUMTEXT NOT NULL,
                                                    excerpt MEDIUMTEXT,
                                                    content LONGTEXT,
                                                    category TINYTEXT,
                                                    rating TINYTEXT,
                                                    bottomhtml LONGTEXT,
                                                    imgurl MEDIUMTEXT,
                                                    url MEDIUMTEXT);'''
        self.mycursor.execute(createtable)


    def process_item(self, item, spider):
        self.store_db(item)
        print('pipline:' + item['course'][0])
        return item

    def store_db(self, item):
        self.mycursor.execute("INSERT INTO courses (course, excerpt, category, bottomhtml, imgurl, url) VALUES (%s,%s,%s,%s,%s,%s);",(item['course'][0],item['excerpt'][0],item['category'][0],item['bottomhtml'][0],item['imgurl'][0],item['url'][0]))
        self.mydb.commit()