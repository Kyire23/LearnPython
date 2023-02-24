"""
@Author = oumuamuanode
@Time : 2022/11/3 15:43
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

    def create_coures(self, course_name):
        course = Course(course_name)
        print(str.format('{0} 创建了{1}课程', self.name, course.name))
        return course

    def create_teacher(self, teacher_name, teacher_passwd):
        teacher = Teacher(teacher_name, teacher_passwd)
        print(str.format('{0}招聘{1}为老师', self.name, teacher.name))
        return teacher


# 教师类
class Teacher(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.courses = list()

    def scoring(self, student, course, grade):
        print("开始打分")
        if course in student.course:
            print(str.format('{0}老师给{1}的{2}打了{3}分',
                             self.name, student.name, course.name, grade))
        else:
            print(str.format('{0}老师发现学生{1}没有选择{2}课程',
                             self.name, student.name, course.name))


# 学校类
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.courses = list()

    def add_course(self, course):
        course_name = course.name
        self.courses.append(course_name)
        print(str.format('{0} 学校增加了{1} 课程', self.name, course_name))


# 课程类
class Course(object):
    def __init__(self, name):
        self.name = name
        self.students = list()


# 学生类
class Student(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.course = list()

    def get_school_list(self, admin):
        print('当前的学校有:')
        for i in admin.school_list:
            print(str.format('{0}', i.name))

    def choice_school(self, school):
        self.school = school
        print(str.format('{0}选择了{1}', self.name, school.name))

    def choice_course(self, course):
        if course.name in self.school.courses:
            self.course.append(course)
            course.students.append(self.name)
            print(str.format('{0}选择了{1}课程', self.name, course.name))
        else:
            print(str.format('{0}没有{1}课程', self.school.name, course.name))


admin = Admin('Admin', '123')

bj_school = admin.create_school('BJ_School', '北京')
sz_school = admin.create_school('SZ_School', '深圳')
sh_school = admin.create_school('SH_School', '上海')
wh_school = admin.create_school('WH_School', '武汉')

python = admin.create_coures('Python')
linux = admin.create_coures('Linux')
java = admin.create_coures('Java')

bj_school.add_course(python)
bj_school.add_course(linux)
bj_school.add_course(java)
sh_school.add_course(java)
sh_school.add_course(python)
wh_school.add_course(linux)
sz_school.add_course(python)
sz_school.add_course(java)

teacher1 = admin.create_teacher('Teacher1', '123')
teacher2 = admin.create_teacher('Teacher2', '123')

# 学生1
student1 = Student('Student1', '123')
student1.get_school_list(admin)
student1.choice_school(sh_school)
student1.choice_course(linux)
student1.choice_course(python)
student1.choice_course(java)


# 学生2


# 人类
class Person(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password


# 管理员类，继承Person
class Admin(Person):
    school_list = []

    def __init__(self, name, password):
        super().__init__(name, password)

    def create_school(self, school_name, school_addr):
        school = School(school_name, school_addr)
        Admin.school_list.append(school)
        print(str.format('{0} 创建了{1}', self.name, school.name))
        return school

    def create_course(self, course_name):
        course = Course(course_name)
        print(str.format('{0}创建了{1}课程', self.name, course.name))
        return course

    def create_teacher(self, teacher_name, teacher_passwd):
        teacher = Teacher(teacher_name, teacher_passwd)
        print(str.format('{0}招聘{1}为老师', self.name, teacher.name))
        return teacher



