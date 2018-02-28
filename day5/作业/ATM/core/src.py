#!/usr/bin/python
#-*- coding:utf-8 –*-




import logging
from lib import common
def shopping():
    print('购物操作')
def check_balance():
    print('查看余额操作')
def transfer():
    print('转账操作')

    log_msg='XXX给xxx转了一笔钱'
    common.logger_handle('转账')
    logging.debug(log_msg)


def pay_back():
    print('还款操作')

