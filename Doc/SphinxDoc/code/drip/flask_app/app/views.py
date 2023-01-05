# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个flask-app的视图函数类，主要包括信息视图功能和插件视图功能
"""
模块介绍
-------

这是一个flask-app的视图函数类，主要包括信息视图功能和插件视图功能

设计模式：

    无

关键点：    

    （1）view

主要功能：            

    （1）为flask-app提供视图函数
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import calendar
from flask import g
from flask_appbuilder import ModelView
### 后来添加的依赖
from flask_appbuilder.api import BaseApi,expose
from flask import redirect
from flask import render_template
from flask import current_app
from config import MINIO_SETTINGS,TTYD_SETTINGS
###
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
### 
from . import appbuilder
# from .models import ContactGroup,Contact,Tags,TestInfo,LogInfo
### 重新添加的数据模型
from .models import AlgorithmInfo,ModelInfo,ParameterInfo,ApplicationInfo,DatasetInfo,LogInfo



####### 视图函数类 ###########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）view                                                             ###
### 主要功能：                                                            ###
### （1）为flask-app提供视图函数                                           ###
############################################################################



####### 视图函数 #####################################################################
#####################################################################################



### algorithm info view
class AlgorithmInfoView(ModelView):
    '''
    类介绍：

        这是一个算法信息视图函数类
    '''

    ### 数据模型
    datamodel = MongoEngineInterface(AlgorithmInfo)
    ### 可展示数据列
    list_columns = ["name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "homepage",
                    "author",
                    "authoremail",
                    "license",
                    "requires",
                    "requiredby",
                    "time"]
    ### 可搜索数据列
    search_columns = ["name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "homepage",
                      "author",
                      "authoremail",
                      "license",
                      "requires",
                      "requiredby",
                      "time"]

    
    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### model info view
class ModelInfoView(ModelView):
    '''
    类介绍：

        这是一个模型信息视图函数类
    '''

    ### 数据模型
    datamodel = MongoEngineInterface(ModelInfo)
    ### 可展示数据列
    list_columns = ["name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "requires",
                    "data",
                    "algorithm",
                    "time"]
    ### 可搜索数据列
    search_columns = ["name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "requires",
                      "data",
                      "algorithm",
                      "time"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### parameter info view
class ParameterInfoView(ModelView):
    '''
    类介绍：

        这是一个参数信息视图函数类
    '''

    ### 数据模型
    datamodel = MongoEngineInterface(ParameterInfo)
    ### 可展示数据列
    list_columns = ["name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "datatype",
                    "requiredby",
                    "time"]
    ### 可搜索数据列
    search_columns = ["name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "datatype",
                      "requiredby",
                      "time"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### application info view
class ApplicationInfoView(ModelView):
    '''
    类介绍：：

        这是一个应用信息视图函数类
    '''

    ### 数据模型
    datamodel = MongoEngineInterface(ApplicationInfo)
    ### 可展示数据列
    list_columns = ["name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "requires",
                    "project",
                    "time"]
    ### 可搜索数据列
    search_columns = ["name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "requires",
                      "project",
                      "time"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### dataset info view
class DatasetInfoView(ModelView):
    '''
    类介绍：

        这是一个数据集信息视图函数类
    '''

    ### 数据模型
    datamodel = MongoEngineInterface(DatasetInfo)
    ### 可展示数据列
    list_columns = ["name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "requiredby",
                    "datatype",
                    "project",
                    "time"]
    ### 可搜索数据列
    search_columns = ["name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "requiredby",
                      "datatype",
                      "project",
                      "time"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### log info view
class LogInfoView(ModelView):
    '''
    类介绍：

        这是一个日志信息视图函数类
    '''

    ### 数据模型
    datamodel = MongoEngineInterface(LogInfo)
    ### 可展示数据列
    list_columns = ["msg",
                    "levelname",
                    "filename",
                    "module",
                    "lineno",
                    "time"]
    ### 可搜索数据列
    search_columns = ["msg",
                      "levelname",
                      "filename",
                      "module",
                      "lineno",
                      "time"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



####### 添加功能视图 #####################################################################
#########################################################################################



### add algorithm info view
appbuilder.add_view(
    AlgorithmInfoView,
    "Algorithm Info View",
    icon="fas fa-cube",
    category="DataInfo",
    category_icon="fas fa-table",
)



### add model info view
appbuilder.add_view(
    ModelInfoView,
    "Model Info View",
    icon="fas fa-puzzle-piece",
    category="DataInfo",
    category_icon="fas fa-table"
)



### add parameter info view
appbuilder.add_view(
    ParameterInfoView,
    "Parameter Info View",
    icon="fas fa-th",
    category="DataInfo",
    category_icon="fas fa-table"
)



### add application info view
appbuilder.add_view(
    ApplicationInfoView,
    "Application Info View",
    icon="fas fa-rocket",
    category="DataInfo",
    category_icon="fas fa-table"    
)



### add dataset info view
appbuilder.add_view(
    DatasetInfoView,
    "Dataset Info View",
    icon="fas fa-database",
    category="DataInfo",
    category_icon="fas fa-table"    
)



### add log info view
appbuilder.add_view(
    LogInfoView,
    "Log Info View",
    icon="fas fa-clipboard",
    category="DataInfo",
    category_icon="fas fa-table"    
)



####### 添加链接视图 ##########################################################################
##############################################################################################



appbuilder.add_link(name='MinIO',
                    href='http://{}:{}'.format(MINIO_SETTINGS['host'],MINIO_SETTINGS['port']),
                    icon='fas fa-archive',
                    category='OperatorPlugin',
                    category_icon='fas fa-plug') ### href 直接写入网络协议即可直接跳转 minio   



appbuilder.add_link(name='ttyd',
                    href='http://{}:{}'.format(TTYD_SETTINGS['host'],TTYD_SETTINGS['port']),
                    icon='fas fa-terminal',
                    category='OperatorPlugin',
                    category_icon='fas fa-plug') ### href 直接写入网络协议即可直接跳转 ttyd



####### 安全清空视图 ##########################################################################
##############################################################################################



appbuilder.security_cleanup()



####### 测试代码 ########################################################################
########################################################################################



# def get_user():
#     return g.user.id


# class HelloApi(BaseApi):

#     route_base = '/api/'
#     @expose('/hello')
#     def hello(self):
#         config = current_app.config
#         minio_settings = config.get('MINIO_SETTINGS')
#         return 'hello world! Minio.{}'.format(minio_settings)

# ### test view
# class TestInfoView(ModelView):
#     datamodel = MongoEngineInterface(TestInfo)
#     list_columns = ["name","version","summary","config","remark","datatype"]
# ### loginfo view
# class LogInfoView(ModelView):
#     datamodel = MongoEngineInterface(LogInfo)
#     list_columns = ["msg","levelname","filename","module","lineno","time"]
#     search_columns = ["filename","module","msg"]


# class ContactModelView(ModelView):
#     datamodel = MongoEngineInterface(Contact)
#     list_columns = ["name", "personal_celphone", "birthday", "contact_group.name"]


# class GroupModelView(ModelView):
#     datamodel = MongoEngineInterface(ContactGroup)
#     related_views = [ContactModelView]
#     search_columns = ["name"]


# class TagsModelView(ModelView):
#     datamodel = MongoEngineInterface(Tags)


# class ContactChartView(GroupByChartView):
#     datamodel = MongoEngineInterface(Contact)
#     chart_title = "Grouped contacts"
#     label_columns = ContactModelView.label_columns
#     chart_type = "PieChart"

#     definitions = [
#         {"group": "contact_group", "series": [(aggregate_count, "contact_group")]},
#         {"group": "gender", "series": [(aggregate_count, "gender")]},
#     ]


# def pretty_month_year(value):
#     return calendar.month_name[value.month] + " " + str(value.year)


# def pretty_year(value):
#     return str(value.year)


# class ContactTimeChartView(GroupByChartView):
#     datamodel = MongoEngineInterface(Contact)

#     chart_title = "Grouped Birth contacts"
#     chart_type = "AreaChart"
#     label_columns = ContactModelView.label_columns
#     definitions = [
#         {
#             "group": "month_year",
#             "formatter": pretty_month_year,
#             "series": [(aggregate_count, "contact_group")],
#         },
#         {
#             "group": "year",
#             "formatter": pretty_year,
#             "series": [(aggregate_count, "contact_group")],
#         },
#     ]


# appbuilder.add_view(
#     GroupModelView,
#     "List Groups",
#     icon="fa-folder-open-o",
#     category="Contacts",
#     category_icon="fa-envelope",
# )
# appbuilder.add_view(
#     ContactModelView,
#     "List Contacts",
#     icon="fa-folder-open-o",
#     category="Contacts",
#     category_icon="fa-envelope",
# )
# appbuilder.add_view(
#     TagsModelView,
#     "List Tags",
#     icon="fa-folder-open-o",
#     category="Contacts",
#     category_icon="fa-envelope",
# )
# appbuilder.add_separator("Contacts")
# appbuilder.add_view(
#     ContactChartView, "Contacts Chart", icon="fa-dashboard", category="Contacts"
# )
# appbuilder.add_view(
#     ContactTimeChartView,
#     "Contacts Birth Chart",
#     icon="fa-dashboard",
#     category="ContactsOne",
# )

# ### add testinfo view
# appbuilder.add_view(TestInfoView,"Test Info View",icon="fa-dashboard",category="Test")
# ### add loginfo view
# appbuilder.add_view(LogInfoView,"Log Info View",icon="fa-dashboard",category="Test")

# ###
# appbuilder.add_api(HelloApi)
# appbuilder.add_link(name='hello',href='/api/hello',icon='fa-dashboard',category='operator',category_icon='fa-dashboard') 
# appbuilder.add_link(name='minio',href='http://{}:{}'.format(MINIO_SETTINGS['host'],MINIO_SETTINGS['port']),icon='fa-dashboard',category='operator',category_icon='fa-dashboard') ### href 直接写入网络协议即可直接跳转 minio    
# appbuilder.add_link(name='ttyd',href='http://{}:{}'.format(TTYD_SETTINGS['host'],TTYD_SETTINGS['port']),icon='fa-dashboard',category='operator',category_icon='fa-dashboard') ### href 直接写入网络协议即可直接跳转 ttyd

# appbuilder.security_cleanup()



######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################


