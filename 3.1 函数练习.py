import random
first =['张','王','李','赵','孙','钱','韩','葛','洪']
second = ['凝','雪','丹','春','虔','璇','安','浩','龙','伟']
def get_random_name():
    x = random.randint(0,len(first))
    y = random.randint(0,len(second))
    name = first[x] + second[y]
    return name

def get_all_name():
    name_list = []
    n = int(input("请输入需要生成的数量:"))
    for i in range(n):
        name = get_random_name()
        name_list.append(name)
    return name_list

name_list = get_all_name()
print(name_list)
