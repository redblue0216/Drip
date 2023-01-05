# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个drip常用命令行接口类
"""
模块介绍
-------

这是一个drip常用命令行接口类

设计模式：

    无

关键点：    

    （1）click 

主要功能：            

    （1）drip程序管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import click
import os
from rich.console import Console
import sys
import drip as dp



####### CLI命令行接口 #######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）click                                                           ###
### 主要功能：                                                            ###
### （1）drip程序管理                                                     ###
############################################################################



###### CLI命令行接口 #####################################################################
#########################################################################################



### drip命令组
@click.group()
@click.help_option('-H','--help')
@click.version_option('-V','--version')
def drip():
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======                    Hello! Welcome to Drip                   ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="blue")



### drip创建管理员用户admin/admin
@click.command(help="drip create adminer")
def create_admin():
    console = Console()
    drip_path = dp.__file__.replace('__init__.py','')### __init__.py前的drip\需要去掉，打包后
    console.print('=================================================================>>>>>> drip create adminer ',style="blue")
    system_platform = sys.platform
    if system_platform == 'win32':
        os.system("{} & cd {} & cd flask_app & flask fab create-admin".format(drip_path[:2],drip_path))  
    elif system_platform == 'linux':
        os.system("cd {} & cd flask_app & flask fab create-admin".format(drip_path)) 



### atom启动后台服务
@click.command(help="drip start webui service")
def start_webui():
    console = Console()
    drip_path = dp.__file__.replace('__init__.py','')### __init__.py前的drip\需要去掉，打包后
    console.print('=================================================================>>>>>> drip start webui service ',style="blue")
    system_platform = sys.platform
    if system_platform == 'win32':
        os.system("{} & cd {} & cd flask_app & python run.py".format(drip_path[:2],drip_path))  
    elif system_platform == 'linux':
        os.system("cd {} & cd flask_app & python run.py".format(drip_path)) 



### 向atom命令组添加命令
drip.add_command(create_admin)
drip.add_command(start_webui)



### python脚本主程化
if __name__ == '__main__':
    console = Console()
    console.print("\n\
                   =========================================================================== \n\
                   =======                                                             ======= \n\
                   =======                    Hello! Welcome to Drip                   ======= \n\
                   =======                                                             ======= \n\
                   ===========================================================================",style="blue")
    drip()



##########################################################################################################################
##########################################################################################################################


