# coding:utf-8
# @Time  : 2019-07-24 16:43
# @Author: Xiawang
import pymysql


def get_data():
    def connect_db():  # 闭包, 保证数据库配置的安全性
        db = pymysql.connect(
            host='10.1.200.166',
            port=3306,
            user='lagouro',
            passwd='Q12_#*s#$opIx',
            db='lagou_commercialization',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = db.cursor()
        return db, cursor

    db, cursor = connect_db()
    db.ping(reconnect=True)
    return db, cursor


def get_product_template(name):
    db, cursor = get_data()
    cursor.execute('select id, name from t_product_template where status = "USED" and name like "{}%"'.format(name))
    return cursor.fetchall()


def get_product_template_id(name):
    db, cursor = get_data()
    cursor.execute('select id from t_product_template where name = "{}"'.format(name))
    template = cursor.fetchall()
    template_id = template[0]['id']
    return template_id


if __name__ == '__main__':
    # print(get_product_template())
    print(get_product_template_id('anan24小时旧版拉勾加模板'))
