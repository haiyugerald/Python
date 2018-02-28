#!/usr/bin/python
#-*- coding:utf-8 –*-

import  logging.config
from conf import settings

# 此方法太low
# def logger(msg):
#     with open(settings.LOG_PATH,'a',encoding='utf-8') as f:
#         f.write('%s\n'%msg)

def logger_handle(log_name):
    logging.config.dictConfig(settings.LOGGING_DIC)  #导入之前定义的logging配置
    logger = logging.getLogger(log_name)   #生成一个log实例
    return  logger