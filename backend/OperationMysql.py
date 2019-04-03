# coding:utf-8
import pymysql


class OperationMysql:
    '''
    封装数据库操作
    '''
    def __init__(self):
        '''
        初始连接数据库, 此数据库部署在测试环境A
        '''
        self.conn = pymysql.connect(
            host='10.1.200.127',
            port=3306,
            user='lagourw',
            passwd='JUY#*f2349Kl',
            db='lagou_resume',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def get_db_data(self, phone):
        '''
        根据caseid找到对应用例内容
        :param case_id: str
        :return: dict
        '''
        case_data = self.search_one("SELECT * FROM r_resume where %s " % phone)
        return case_data




    def search_one(self, sql):
        '''
        执行SQL语句, 返回一条结果, 再次执行返回下一个结果
        :param sql: str, sql语句
        :return: dict
        '''
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def search_all(self, sql):
        '''
        执行SQL语句, 获取全部数据
        :param sql: str, sql语句
        :return: dict
        '''
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def update_all(self, sql):
        try:
            self.cur.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            self.conn.rollback()


if __name__ == '__main__':
    op_mysql = OperationMysql()
    # res = op_mysql.get_db_data(13300000011)
    # args={'userid':537}
    # res = op_mysql.search_one("SELECT id FROM r_resume where userId = %d " % args['userid'])
    res = op_mysql.update_all('UPDATE r_resume set sex = "男" WHERE id = 1')
    print(res)
