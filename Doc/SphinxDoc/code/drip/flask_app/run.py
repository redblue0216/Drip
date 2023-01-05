# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个flask-app的运行管理类
"""
模块介绍
-------

这是一个flask-app的运行类

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供运行管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from app import app
import yaml
# import drip as dp



####### 配置管理 ############################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供配置功能                                           ###
#############################################################################



####### 运行管理 ###################################################################
###################################################################################



### 从配置文件中获取具体配置信息
# drip_package_path = dp.__file__.replace('__init__.py','')
drip_package_path = '../'
drip_config_file = open('{}drip_config.yaml'.format(drip_package_path),encoding='UTF-8')
drip_config_yaml = yaml.load(drip_config_file,Loader=yaml.FullLoader)
dirp_webui_port = drip_config_yaml['drip_webui_port']
drip_web_host = drip_config_yaml['drip_webui_host']
app.run(host=drip_web_host, port=dirp_webui_port, debug=True)



#######################################################################################
#######################################################################################


