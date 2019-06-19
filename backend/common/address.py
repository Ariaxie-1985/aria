# coding:utf-8
# @Time  : 2019-06-14 19:02
# @Author: Xiawang

import pymysql


def connect_testing_platform():
    db = pymysql.connect(
        host='10.1.200.166',
        port=3306,
        user='lagouro',
        passwd='Q12_#*s#$opIx',
        db='testing_platform',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()
    return db, cursor


def connect_mds_position():
    db = pymysql.connect(
        host='10.1.200.166',
        port=3306,
        user='lagourw',
        passwd='JUY#*f2349Kl',
        db='mds_position',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()
    return db, cursor


def junge_address(address):
    db, cursor = connect_testing_platform()
    db.ping(reconnect=True)
    cursor.execute(
        "SELECT id FROM t_work_address WHERE CONCAT(city,district,detail_address) = '{}'".format(
            address))
    results = cursor.fetchall()[0]['id']
    db.close()
    return results
