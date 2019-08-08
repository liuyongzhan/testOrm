from django.db import models


# 学生类
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    # 一对多外键设置，'多'的模型类设置外键，注意需要带参数on_delete
    myClass = models.ForeignKey('Class', on_delete=models.CASCADE)
    # 一对一外键设置，哪个模型设置外键都可以，注意需要带参数on_delete
    detail = models.OneToOneField('StudentDetail', on_delete=models.CASCADE)

# 学生信息类
class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    blog = models.CharField(max_length=100)

# 班级类
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=50)

# 老师类
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    # 多对多外键设置，哪个模型类创建外键都可以，注意没有on_delete参数
    myClass = models.ManyToManyField(Class)