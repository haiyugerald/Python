#!/usr/bin/python
#-*- coding:utf-8 –*-
# xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，
# 不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，
# 至今很多传统公司如金融行业的很多系统的接口还主要是xml。

# xml就是通过 <> 节点来区别数据结构的:
# xml协议在各个语言里的都是支持的，在python中可以用以下模块操作xml：

# print(root.iter('year')) #全文搜索
# print(root.find('country')) #在root的子节点找，只找一个
# print(root.findall('country')) #在root的子节点找，找所有

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

# 三个部分：tag，attrib，text
# 遍历xml文档
# for child in root:
#     print('========>', child.tag, child.attrib, child.attrib['name'])
#     for i in child:
#         print(i.tag, i.attrib, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated', 'yes')
    node.set('version', '1.0')
tree.write('test.xml')

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

# 在country内添加（append）节点year2
import xml.etree.ElementTree as ET
tree = ET.parse("a.xml")
root = tree.getroot()
for country in root.findall('country'):
    for year in country.findall('year'):
        if int(year.text) > 2000:
            year2 = ET.Element('year2')
            year2.text = '新年'
            year2.attrib = {'update': 'yes'}
            country.append(year2)  # 往country节点下添加子节点

tree.write('a.xml.swap')