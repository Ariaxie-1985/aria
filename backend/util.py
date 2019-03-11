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
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='lagoutest',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("?????????")
        self.cur = self.conn.cursor()

    def get_case_data(self, case_id):
        '''
        根据caseid找到对应用例内容
        :param case_id: str
        :return: dict
        '''
        case_data = self.search_one("SELECT * FROM api_testcase WHERE id = %s" % case_id)
        return case_data

    def insert_user(self,username,role,account):
        '''
        新增用户
        :param username:
        :param role:
        :param account:
        :return:
        '''
        print(username)
        user=self.cur.execute("INSERT INTO `test`.`userlist`(`userid`,`username`,`role`,`account`) VALUES (NULL,'"+username+","+role+","+account+")")
        print(user)
        return user


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


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("SELECT * FROM api_testcase")
    print(res)
