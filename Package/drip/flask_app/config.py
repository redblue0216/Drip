# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个flask-app的配置类，主要包括后端数据库和前端主题相关配置
"""
模块介绍
-------

这是一个flask-app的配置类，主要包括后端数据库和前端主题相关配置

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供配置功能
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import os
import yaml
# import drip as dp



####### 配置管理 ############################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供配置功能                                           ###
############################################################################



####### 配置整理 #######################################################################
#######################################################################################



### 从配置文件中获取具体配置信息
# drip_package_path = dp.__file__.replace('__init__.py','')
drip_package_path = '../'
drip_config_file = open('{}drip_config.yaml'.format(drip_package_path),encoding='UTF-8')
drip_config_yaml = yaml.load(drip_config_file,Loader=yaml.FullLoader)
drip_mongo_db = drip_config_yaml['drip_mongo_db']
drip_mongo_host = drip_config_yaml['drip_mongo_host']
drip_monngo_port = drip_config_yaml['drip_mongo_port']
drip_mongo_username = drip_config_yaml['drip_mongo_username']
drip_mongo_password = drip_config_yaml['drip_mongo_password']
drip_minio_host = drip_config_yaml['drip_minio_host']
drip_minio_port = drip_config_yaml['drip_minio_port']
drip_ttyd_host = drip_config_yaml['drip_ttyd_host']
drip_ttye_port = drip_config_yaml['drip_ttyd_port']




### 基础配置
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"},
    {"name": "Yahoo", "url": "https://me.yahoo.com"},
    {"name": "AOL", "url": "http://openid.aol.com/<username>"},
    {"name": "Flickr", "url": "http://www.flickr.com/<username>"},
    {"name": "MyOpenID", "url": "https://www.myopenid.com"},
]

MONGODB_SETTINGS = {"DB": drip_mongo_db,
                    "host":drip_mongo_host,
                    "port":drip_monngo_port,
                    "username":drip_mongo_username,
                    "password":drip_mongo_password}
                    
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_FOLDER = "translations"
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
}


### 主题配置
# ------------------------------
# GLOBALS FOR GENERAL APP's
# ------------------------------
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
AUTH_TYPE = 1
# AUTH_LDAP_SERVER = "ldap://dc.domain.net"
# AUTH_LDAP_USE_TLS = False
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "Drip"# "F.A.B. Example"
APP_THEME = ""  # default
# APP_THEME = "cerulean.css"      # COOL
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"       # COOL
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"          # COOL
# APP_THEME = "spacelab.css"      # NICE
# APP_THEME = "united.css"


### 扩展配置
### MinIO settings
MINIO_SETTINGS = {'host':drip_minio_host,
                  'port':drip_minio_port}


### ttyd settings
TTYD_SETTINGS = {'host':drip_ttyd_host,
                 'port':drip_ttye_port}



##############################################################################################
##############################################################################################


