# -*- coding : utf-8 -*-
# @Timer : 2023/4/25 11:28
# File : test.py


teachers = ['李老师','王老师','赵老师','张老师','钱老师','董老师','顾老师','葛老师']
classroom = [[],[],[]]
'''
思路一：从teacher循环遍历每个元素，随机存放到教室里
'''
import random

for i in teachers:
    index = random.randint(0,2)
    classroom[index].append(i)
print(classroom)
# with open('result.txt','w'):
#     pass
with open('result.txt', 'w+', encoding='utf-8') as file:
    for j in range(len(classroom)):
        name = ','.join(classroom[j])
        file.write(f'第{j + 1}个教室的老师有：{name}')
        file.write('\n')