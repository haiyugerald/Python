#!/usr/bin/python
#-*- coding:utf-8 –*-
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod  #指明下面的函数在他的继承类必须有同一名称的函数
    def run(self):
        pass
    @abc.abstractclassmethod
    def sleep(self):
        pass
    @abc.abstractclassmethod
    def eat(self):
        pass

class People(Animal):
    def run(self):
        print('People run')
    def sleep(self):
        print('People sleep')
    def eat(self):
        print('People eat')

peo1=People()
peo1.sleep()