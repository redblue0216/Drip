# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个flask-app的数据模型类，主要包括算法信息、模型信息、参数信息、应用信息、数据集信息和日志信息六大数据模型
"""
模块介绍
-------

这是一个flask-app的数据模型类，主要包括算法信息、模型信息、参数信息、应用信息、数据集信息和日志信息六大数据模型

设计模式：

    无

关键点：    

    （1）mongoengine

主要功能：            

    （1）为flask-app提供数据模型
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import datetime
from mongoengine import Document
from mongoengine import (
    DateTimeField,
    IntField,
    StringField,
    ReferenceField,
    ListField,
    FileField,
    ImageField,
)



####### 数据模型类 ###########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）mongoengine                                                      ###
### 主要功能：                                                            ###
### （1）为flask-app提供数据模型                                          ###
############################################################################



####### 具体数据信息类 ###########################################################
#################################################################################



### algorithm info
class AlgorithmInfo(Document):
    '''
    类介绍：

        这是一个算法信息数据模型类
    '''

    name = StringField(max_length=100)
    version = StringField(max_length=100)
    summary = StringField(max_length=500)
    config = StringField(max_length=500)
    remark = StringField(max_length=500)
    homepage = StringField(max_length=100)
    author = StringField(max_length=100)
    authoremail = StringField(max_length=100)
    license = StringField(max_length=100)
    requires = StringField(max_length=500)
    requiredby = StringField(max_length=100)
    time = DateTimeField(unique=True)



### model info
class ModelInfo(Document):
    '''
    类介绍：

        这是一个模型信息数据模型类
    '''

    name = StringField(max_length=100)
    version = StringField(max_length=100)
    summary = StringField(max_length=500)
    config = StringField(max_length=500)
    remark = StringField(max_length=500)
    requires = StringField(max_length=500)
    data = StringField(max_length=100)
    algorithm = StringField(max_length=100)
    time = DateTimeField(unique=True)



### parameter info
class ParameterInfo(Document):
    '''
    类介绍：

        这是一个参数信息数据模型类
    '''

    name = StringField(max_length=100)
    version = StringField(max_length=100)
    summary = StringField(max_length=500)
    config = StringField(max_length=500)
    remark = StringField(max_length=500)
    datatype = StringField(max_length=100)
    requiredby = StringField(max_length=100)
    time = DateTimeField(unique=True)


### application info
class ApplicationInfo(Document):
    '''
    类介绍：

        这是一个应用信息数据模型类
    '''

    name = StringField(max_length=100)
    version = StringField(max_length=100)
    summary = StringField(max_length=500)
    config = StringField(max_length=500)
    remark = StringField(max_length=500)
    requires = StringField(max_length=500)
    project = StringField(max_length=100)
    time = DateTimeField(unique=True)



### dataset info
class DatasetInfo(Document):
    '''
    类介绍：

        这是一个数据集信息数据模型类
    '''

    name = StringField(max_length=100)
    version = StringField(max_length=100)
    summary = StringField(max_length=500)
    config = StringField(max_length=500)
    remark = StringField(max_length=500)
    requiredby = StringField(max_length=100)
    datatype = StringField(max_length=100)
    project = StringField(max_length=100)
    time = DateTimeField(unique=True)
    


### log info
class LogInfo(Document):
    '''
    类介绍：

        这是一个日志信息数据模型类
    '''

    msg = StringField(max_length=500)
    levelname = StringField(max_length=100)
    filename = StringField(max_length=100)
    module = StringField(max_length=100)
    lineno = IntField(min_value=0)
    time = DateTimeField(unique=True)
    # time = StringField(max_length=100)



####### 测试代码 ################################################################
################################################################################



# ### test data model
# class TestInfo(Document):
#     name = StringField(max_length=100)
#     version = StringField(max_length=100)
#     summary = StringField(max_length=100)
#     config = StringField(max_length=100)
#     remark = StringField(max_length=100)
#     datatype = StringField(max_length=100)
#     requiredby = StringField(max_length=100) 


# mindate = datetime.date(datetime.MINYEAR, 1, 1)


# class ContactGroup(Document):
#     name = StringField(max_length=60, required=True, unique=True)

#     def __unicode__(self):
#         return self.name

#     def __repr__(self):
#         return self.name


# class Gender(Document):
#     name = StringField(max_length=60, required=True, unique=True)

#     def __unicode__(self):
#         return self.name

#     def __repr__(self):
#         return self.name

#     def __str__(self):
#         return self.name


# class Tags(Document):
#     meta = {"allow_inheritance": True}

#     name = StringField(max_length=60, required=True, unique=True)

#     def __unicode__(self):
#         return self.name


# class Contact(Document):
#     name = StringField(max_length=60, required=True, unique=True)
#     address = StringField(max_length=60)
#     birthday = DateTimeField()
#     personal_phone = StringField(max_length=20)
#     personal_celphone = StringField(max_length=20)
#     contact_group = ReferenceField(ContactGroup, required=True)
#     # gender = ReferenceField(Gender, required=True)
#     tags = ListField(ReferenceField(Tags))

#     def month_year(self):
#         date = self.birthday or mindate
#         return datetime.datetime(date.year, date.month, 1) or mindate

#     def year(self):
#         date = self.birthday or mindate
#         return datetime.datetime(date.year, 1, 1)

#     def __repr__(self):
#         return "%s : %s\n" % (self.name, self.contact_group)



#######################################################################################
#######################################################################################


