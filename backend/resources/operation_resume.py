# coding:utf-8
# @Time  : 2019-04-02 11:29
# @Author: Xiawang
from flask_restful import Resource, reqparse

from backend.OperationMysql import OperationMysql

op_mysql = OperationMysql()


class getResume(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, help="请输入正确手机号")
        parser.add_argument('userid', type=str, help="请输入正确userid")
        args = parser.parse_args()
        if args['phone']:
            try:
                resume_id = op_mysql.search_one(
                    "SELECT id FROM r_resume WHERE phone = %s" %
                    args['phone'])
                state = 1
                info = resume_id[0]
                global resumeid
                resumeid = resume_id[0]['id']
            except BaseException:
                state = 400
                info = "找不到简历id, 请确认下手机号填写是否正确"
        elif args['userid']:
            try:
                resume_id = op_mysql.search_one(
                    "SELECT id FROM r_resume WHERE userId = %d" % int(
                        args['userid']))
                state = 1
                info = resume_id
                resumeid = resume_id['id']
            except BaseException:
                state = 400
                info = "找不到简历id, 请确认下userid填写是否正确"
        if resumeid:
            basicMain = op_mysql.search_one(
                "SELECT * FROM r_resume WHERE id = %s " %
                resumeid)
            basicMain['createTime'] = str(basicMain['createTime'])
            basicMain['updateTime'] = str(basicMain['updateTime'])
            workExperience = op_mysql.search_one(
                "SELECT * FROM r_work_experience WHERE resumeId = %s AND isDel = 0 ORDER BY createTime desc" %
                resumeid)
            for work_Ex in workExperience:
                work_Ex['createDate'] = str(work_Ex['createDate'])
            educationExperience = op_mysql.search_one(
                "SELECT * FROM r_education_experience WHERE resumeId = %s AND isDel = 0 ORDER BY createDate desc" %
                resumeid)
            for ed_Ex in educationExperience:
                ed_Ex['createDate'] = str(ed_Ex['createDate'])

            ability_label = op_mysql.search_all(
                "SELECT * FROM r_ability_label WHERE resume_id = %s AND is_del = 0" %
                resumeid)
            for ab_label in ability_label:
                ab_label['create_time'] = str(ab_label['create_time'])
                ab_label['update_time'] = str(ab_label['update_time'])

            r_expect_jobs = op_mysql.search_one(
                "SELECT * FROM r_expect_jobs where resumeId = %s" %
                resumeid)
            r_expect_jobs['createDate'] = str(basicMain['createTime'])
            r_expect_jobs['updateTime'] = str(basicMain['updateTime'])
            info = "操作成功！"

        return {
            'state': state,
            'content': info,
            'result': {
                'basicMain': basicMain,
                'workExperience': workExperience,
                'educationExperience': educationExperience,
                'ability_label': ability_label}}

    def post(self):
        parser = reqparse.RequestParser()
        ''' 基本信息 '''
        parser.add_argument('id', type=int, help="简历id")
        parser.add_argument('name', type=str, help="姓名")
        parser.add_argument('sex', type=str, help="性别, 例如 男、女")
        parser.add_argument('birthday', type=str, help="生日, 例如 1990.07")
        parser.add_argument('email', type=str, help="邮箱")
        parser.add_argument('liveCity', type=str, help="所在城市")
        parser.add_argument('work_year', type=str, help="工作年份")
        parser.add_argument('joinWorkTime', type=str, help="参加工作时间")
        ''' 工作经历 '''
        parser.add_argument('companyName', type=str, help="公司名称")
        parser.add_argument('department', type=str, help="所属部门")
        parser.add_argument('positionType', type=str, help="职位类型")
        parser.add_argument('positionName', type=str, help="职位名称")
        parser.add_argument('startDate', type=str, help="入职时间")
        parser.add_argument('endDate', type=str, help="离职时间")
        parser.add_argument('companyIndustry', type=str, help="行业标签")
        parser.add_argument('skillLabel', type=str, help="技能标签")
        parser.add_argument('workContent', type=str, help="工作内容")
        ''' 教育经历 '''
        parser.add_argument('schoolName', type=str, help="学校名称")
        parser.add_argument('professional', type=str, help="专业")
        parser.add_argument('startDate', type=str, help="入学年份")
        parser.add_argument('endDate', type=str, help="毕业年份")
        parser.add_argument('education', type=str, help="学历")
        ''' 个人名片 '''
        parser.add_argument('label_name', type=str, help="综合能力标签")
        parser.add_argument('myRemark', type=str, help="自我描述")
        ''' 求职意向 '''
        parser.add_argument('positionName', type=str, help="期望职位")
        parser.add_argument('positionType', help="职位类型")
        parser.add_argument('salarys', type=str, help="期望薪资")
        parser.add_argument('city', type=str, help="期望城市")
        parser.add_argument('status', type=str, choice=('积极找工作', '随便看看', '暂时不换工作'), help="当前状态")
        parser.add_argument('arrivalTime', type=str, choice=('随时', '2周以内', '2周-1个月', '1-3个月', '3个月以上'), help="到岗时间")

        args = parser.parse_args()

        op_mysql.update_all(
            'UPDATE r_resume set name = %s,sex = %s,birthday=%s,email=%s,liveCity=%s,work_year=%s joinWorkTime=%s WHERE id = %d' %
            args['name'], args['sex'], args['birthday'], args['email'], args['liveCity'], args['work_year'],
            args['joinWorkTime'], int(args['id']))

        positionType1 = args['positionType'][0]
        positionType2 = args['positionType'][1]
        positionType = args['positionType'][2]

        op_mysql.update_all(
            'UPDATE r_work_experience set companyName = %s,department = %s,positionType1 = %s,positionType2 = %s,positionType=%s,positionName=%s,startDate=%s,endDate=%s,companyIndustry=%s,skillLabel=%s,workContent=%s  WHERE id = %d' %
            args['companyName'],
            args['department'],
            positionType1,
            positionType2,
            positionType,
            args['positionName'],
            args['startDate'],
            args['endDate'],
            args['companyIndustry'],
            args['skillLabel'],
            args['workContent'],
            int(args['id']))

        op_mysql.update_all(
            'UPDATE r_education_experience set schoolName = %s,professional = %s,startDate=%s,endDate=%s,education=%s WHERE id = %d' %
            args['schoolName'], args['professional'], args['startDate'], args['endDate'], args['education'],
            int(args['id']))

        op_mysql.update_all(
            'UPDATE r_ability_label set label_name = %s,myRemark = %s WHERE id = %d' %
            args['label_name'], args['myRemark'], int(args['id']))

        positionNameType1 = args['positionType'][0]
        positionNameType2 = args['positionType'][1]
        positionName = args['positionType'][2]

        op_mysql.update_all(
            'UPDATE r_expect_jobs set positionName = %s,positionNameType1 = %s,positionNameType2=%s,positionName=%s,salarys=%s,city=%s,status=%s,arrivalTime=%s WHERE id = %d' %
            positionName, positionNameType1, positionNameType2, positionName, args['salarys'], args['city'],
            args['status'], args['arrivalTime'], int(args['id']))

        return {'state':1, 'content':'修改完成, 请查询看看是否成功'}
