"""
@Author = oumuamuanode
@Time : 2022/11/3 14:19
"""
class Person(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Admin(Person):
    school_list = []

    def __init__(self, name, password):
        super().__init__(name, password)

    def create_school(self, school_name, school_addr):
        school = School(school_name, school_addr)
        Admin.school_list.append(school)
        print(str.format('{0} 创建了{1}', self.name, school.name))
        return school

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.courses = list()

    def add_course(self, course):
        course_name = course.name
        self.courses.append(course_name)
        print(str.format('{0} 学校增加了{1} 课程', self.name, course_name))

admin = Admin('Admin', '123')

bj_school = admin.create_school('BJ_School','北京')
sz_school = admin.create_school('SZ_School','深圳')
sh_school = admin.create_school('SH_School','上海')
wh_school = admin.create_school('WH_School','武汉')