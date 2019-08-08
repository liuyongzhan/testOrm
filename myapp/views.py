from django.shortcuts import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models import F, Q

from myapp.models import Student, StudentDetail, Class, Teacher

def index(request):
    # 一对一：Student ---> StudentDetail
    # 正向
    print(model_to_dict(Student.objects.filter(id__gt=2)[0].detail))
    # 调用学生对象的detail属性，该属性表示外键映射副表中对应的对象
    # 执行结果：{'id': 3, 'height': 176, 'weight': 60, 'blog': 'http://blog.hq.com'}
    print(serializers.serialize('json', StudentDetail.objects.filter(student__id__gt=5)))
    # 过滤学生信息表查询数据，过滤参数为 "主表名(全小写)__条件"
    # 执行结果：[{"model": "myapp.studentdetail", "pk": 6, "fields": {"height": 180, "weight": 90, "blog": "http://blog.zxl.com"}},
    #            {"model": "myapp.studentdetail", "pk": 7, "fields": {"height": 165, "weight": 75, "blog": "http://blog.ghj.com"}}]

    # 反向
    print(model_to_dict(StudentDetail.objects.get(id=2).student))
    # 这个同上--但是副表要调用对应主表的信息对象，需要使用 .主表名(全小写)
    # 执行结果：{'id': 2, 'name': 'xyl', 'myClass': 1, 'detail': 2}
    print(serializers.serialize('json', Student.objects.filter(detail__id__exact=2)))
    # 同上--主表调用副表直接使用添加外键的属性detail就行，这个属性就是副表中对应的一条数据对象
    # 执行结果：[{"model": "myapp.student", "pk": 2, "fields": {"name": "xyl", "myClass": 1, "detail": 2}}]

    # 一对多：Student ---> Class
    # 正向：
    print(model_to_dict(Student.objects.get(id=3).myClass))
    # 使用主表添加的外键属性，获取副表中的对应数据对象
    # 执行结果：{'id': 2, 'name': 'zhongban', 'desc': 'two'}
    print(serializers.serialize('json', Class.objects.filter(student__id=3)))
    # 副表过滤主表条件的参数，使用student可以调用主表对象，student__id是调用的student对象的id进行筛选
    # 执行结果：[{"model": "myapp.class", "pk": 2, "fields": {"name": "zhongban", "desc": "two"}}]

    # 反向
    print(serializers.serialize('json', Class.objects.get(id=1).student_set.all()))
    # 副表调用主表信息，使用 主表名(全小写)__set,这个其实是一个副表对象在主表中的映射管理器，类似Student.objtects中的objects，这儿objects是控制管理器
    # 执行结果：[{"model": "myapp.student", "pk": 1, "fields": {"name": "lyz", "myClass": 1, "detail": 1}},
    #            {"model": "myapp.student", "pk": 2, "fields": {"name": "xyl", "myClass": 1, "detail": 2}}]
    print(serializers.serialize('json', Student.objects.filter(myClass__id=1)))
    # 这个同上
    # 执行结果：[{"model": "myapp.student", "pk": 1, "fields": {"name": "lyz", "myClass": 1, "detail": 1}},
    #            {"model": "myapp.student", "pk": 2, "fields": {"name": "xyl", "myClass": 1, "detail": 2}}]

    # 多对多：Teacher ---> Class
    # 正向：
    print(serializers.serialize('json', Teacher.objects.get(id=3).myClass.all()))
    # 多对多其实可以对应一对多，两者大体一致，只不过主表的外键属性和副表的teacher__set都是相应的映射管理器，它内部其实都是对应的中间表的进行的关联映射
    # 执行结果：[{"model": "myapp.class", "pk": 3, "fields": {"name": "daban", "desc": "three"}}]
    print(serializers.serialize('json', Class.objects.filter(teacher__id=3)))
    # 过滤班级老师中间表查询数据，过滤参数为 "表名(全小写)__条件"
    # 执行结果：[{"model": "myapp.class", "pk": 3, "fields": {"name": "daban", "desc": "three"}}]

    # 反向
    print(serializers.serialize('json', Class.objects.get(id=1).teacher_set.all()))
    # 如果不在外键的字段中设置related_name的话，默认就用表名_set。
    # 如果设置了related_name="teachers"，反向查询时可直接使用teachers进行反向查询。
    # 执行结果：[{"model": "myapp.teacher", "pk": 1, "fields": {"name": "yuwenlaoshi", "myClass": [1, 2, 3, 4, 5]}},
    #            {"model": "myapp.teacher", "pk": 2, "fields": {"name": "shuxuelaoshi", "myClass": [1, 2, 3]}}]
    print(serializers.serialize('json', Teacher.objects.filter(~Q(myClass__id=2))))
    # 这儿使用到了Q查询，当使用或的条件查询语句时使用，并且F,Q查询与关键字参数一起使用时，F,Q查询必须写到关键字参数前面
    # 执行结果：[{"model": "myapp.teacher", "pk": 3, "fields": {"name": "yingyulaoshi", "myClass": [3]}}]

    # 补充============
    # 多对多关系模型添加移除中间表关系 Teacher ---> Class
    # 本质是给中间表添加，移除数据
    # 正向：
    # 移除
    Teacher.objects.get(id=1).myClass.remove(*Class.objects.filter(id__gt=3))
    # 添加
    Teacher.objects.get(id=1).myClass.add(*Class.objects.filter(id__gt=3))
    # 清空对象关系
    Teacher.objects.get(id=1).myClass.clear()
    # 重新设置关系
    Teacher.objects.get(id=1).myClass.set(list(Class.objects.filter(id__gt=0)))  # 参数为一个可迭代对象就可以

    Class.objects.get(id=5).teacher_set.add(Teacher.objects.get(id=2))
    # 在多对多中通过add添加外键映射关系，并且在中间表中生成对应关系数据

    return HttpResponse("success")
