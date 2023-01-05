# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个flask-app的基础应用管理类
"""
模块介绍
-------

这是一个flask-app的基础应用管理类

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供基础应用管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import logging

from flask import Flask

from flask_appbuilder import AppBuilder
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_mongoengine import MongoEngine
### 
from app.index import MyIndexView



####### 基础应用管理 ##########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供基础应用管理                                        ###
#############################################################################



####### 基础应用管理 ###################################################################
#######################################################################################



logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)#,template_folder='./app/templates')
app.config.from_object("config")
dbmongo = MongoEngine(app)
appbuilder = AppBuilder(app, security_manager_class=SecurityManager,indexview=MyIndexView)


from . import models, views  # noqa



##########################################################################################
##########################################################################################


