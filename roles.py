#定义Roles类


class Roles:
    def __init__(self):
        self.name = ''
        self.sex = ''
        self.nick = ''
        self.inf = ''
        self.times = ''
        self.span = ''


# 寻找列表中的角色名
def searchbyname(rolelist,name):
    for item in rolelist:
        if item.name == name:
            return True


# 添加角色信息
def Add(rolelist, role):
    rolelist.append(role)
    print(role.name, role.sex, role.nick, role.inf, role.times,role.span)
    file_object = open('roles.txt', 'a')
    file_object.write(role.name)
    file_object.write(' ')
    file_object.write(role.sex)
    file_object.write(' ')
    file_object.write(role.nick)
    file_object.write(' ')
    file_object.write(role.inf)
    file_object.write(' ')
    file_object.write(str(role.times))
    file_object.write(' ')
    file_object.write(str(role.span))
    file_object.write('\n')
    file_object.close()
    print("保存成功")


# 利用姓名寻找角色信息
def search1(rolelist,name):
    print("{0:{6}^6}{1:{6}^10}{2:{6}^11}{3:{6}^25}{4:{6}^12}{5:{6}^10}".format("姓名", "性别", "别名", "基本信息", "出现次数", "篇幅跨度",
                                                                               chr(12288)))
    count = 0
    for item in rolelist:
        if item.name == name:
                if item.nick == 'None':
                    print("{0:{6}^6}{1:{6}^10}{2:{6}^12}{3:{6}^26}{4:{6}^13}{5:{6}^12}".format(item.name, item.sex,
                                                                                               item.nick,
                                                                                               item.inf, item.times,
                                                                                               item.span,
                                                                                               chr(12288)))
                else:
                    print("{0:{6}^6}{1:{6}^10}{2:{6}^10}{3:{6}^25}{4:{6}^14}{5:{6}^11}".format(item.name, item.sex,
                                                                                               item.nick,
                                                                                               item.inf, item.times,
                                                                                               item.span,
                                                                                               chr(12288)))
                    break
        count = 0
    if count == len(rolelist):
        print('查无此人')


# 利用别名寻找角色信息
def search2(rolelist,nick):
    print("{0:{6}^6}{1:{6}^10}{2:{6}^11}{3:{6}^25}{4:{6}^12}{5:{6}^10}".format("姓名", "性别", "别名", "基本信息", "出现次数", "篇幅跨度",
                                                                               chr(12288)))
    count = 0
    for item in rolelist:
        if item.nick == nick:
                if item.nick == 'None':
                    print("{0:{6}^6}{1:{6}^10}{2:{6}^12}{3:{6}^26}{4:{6}^13}{5:{6}^12}".format(item.name, item.sex,
                                                                                               item.nick,
                                                                                               item.inf, item.times,
                                                                                               item.span,
                                                                                               chr(12288)))
                else:
                    print("{0:{6}^6}{1:{6}^10}{2:{6}^10}{3:{6}^25}{4:{6}^14}{5:{6}^11}".format(item.name, item.sex,
                                                                                               item.nick,
                                                                                               item.inf, item.times,
                                                                                               item.span,
                                                                                               chr(12288)))
                    break
        count = 0
    if count == len(rolelist):
        print('查无此人')


# 删除已存角色信息
def Del(rolelist,name):
    for item in rolelist:
        if name not in item.name:
            flag = 0
        else:
            flag = 1
            break
    if flag == 1 :
        rolelist.remove(item)
        print('删除成功')
    else:
        print('查无此人！')

    if flag:
        file_object = open('roles.txt', 'w')
        for role in rolelist:
            file_object.write(role.name)
            file_object.write(' ')
            file_object.write(role.sex)
            file_object.write(' ')
            file_object.write(role.nick)
            file_object.write(' ')
            file_object.write(role.inf)
            file_object.write(' ')
            file_object.write(str(role.times))
            file_object.write(' ')
            file_object.write(str(role.span))
            file_object.write('\n')
        file_object.close()


# 亲密度计算
def qinmi(rolelist):
    x = input("请输入要查询的角色:")
    for item in rolelist:
        if x == item.name or x == item.nick:
            flag = 1
            new_x = item
            if x == item.name:
                for i in range(1, 121):
                    f = open('./data/chapter-{}.txt'.format(i), encoding='utf-8', errors='ignore')
                    contents = f.read()
                    if item.nick in contents and item.name not in contents:
                        x = item.nick
                    if item.nick not in contents and item.name in contents:
                        x = item.name
                    if item.nick in contents and item.name in contents:
                        x = item.name
            if x == item.nick:
                for i in range(1, 121):
                    f = open('./data/chapter-{}.txt'.format(i), encoding='utf-8', errors='ignore')
                    contents = f.read()
                    if item.nick in contents and item.name not in contents:
                        x = item.nick
                    if item.nick not in contents and item.name in contents:
                        x = item.name
                    if item.nick in contents and item.name in contents:
                        x = item.nick
            break
        else:
            flag = 0
    if flag == 0:
        print('查无此人！')
    else:
        new_rolelist = rolelist[:]      #创建rolelist的一个拷贝
        new_rolelist.remove(new_x)      #删除要查询的角色
        for item in new_rolelist:       #遍历新列表（除查询角色）
            y = item.name
            z = item.nick
            count = 0
            for i in range(1, 121):
                f = open('./data/chapter-{}.txt'.format(i), encoding='utf-8', errors='ignore')
                contents = f.read()
                if x in contents and (y in contents or z in contents):
                    count += 1
                f.close()
            print(y, count)


# 重写入角色信息
def change(rolelist,name):
    for item in rolelist:
        if item.name == name:
            rolelist.remove(item)
            file_object = open("roles.txt", 'w')
            for role in rolelist:
                file_object.write(role.name)
                file_object.write(' ')
                file_object.write(role.sex)
                file_object.write(' ')
                file_object.write(role.nick)
                file_object.write(' ')
                file_object.write(role.inf)
                file_object.write(' ')
                file_object.write(str(role.times))
                file_object.write(' ')
                file_object.write(str(role.span))
                file_object.write('\n')
            file_object.close()
            role = Roles()
            role.name = input("输入角色姓名:")
            role.times = 0
            while True:
                role.sex = input("请输入该角色性别:")
                break
            while True:
                role.nick = input("请输入该角色的别名:")
                b = range(1, 121)
                for i in b:
                    f = open('./data/chapter-{}.txt'.format(i), encoding='utf-8', errors='ignore')
                    contents = f.read()
                    num = contents.count(role.name)+contents.count(role.nick)
                    role.times += num
                for j in b:
                    f = open('./data/chapter-{}.txt'.format(j), encoding='utf-8', errors='ignore')
                    contents = f.read()
                    if role.name in contents or role.nick in contents:
                        break
                for k in reversed(b):
                    f = open('./data/chapter-{}.txt'.format(k), encoding='utf-8', errors='ignore')
                    contents = f.read()
                    if role.name in contents or role.nick in contents:
                        break
                role.span = k - j
                break
            while True:
                role.inf = input("请输入该角色的基本信息:")
                break
            Add(rolelist, role)


# 出现次数排序（正）
def times_reduce(rolelist):
    print("按出现次数高－低显示")
    mit = sorted(rolelist, key=get_times, reverse=True)
    display(mit)


# 出现次数排序（反）
def times_rise(rolelist):
    print("按出现次数低－高显示")
    mit = sorted(rolelist, key=get_times)
    display(mit)


# 篇幅跨度排序（正）
def span_reduce(rolelist):
    print("按篇幅跨度高－低显示：")
    mit = sorted(rolelist, key=get_span, reverse=True)
    display(mit)


# 篇幅跨度排序（反）
def span_rise(rolelist):
    print("按篇幅跨度低－高显示：")
    mit = sorted(rolelist, key=get_span)
    display(mit)


# 获取角色出现次数
def get_times(*rolelist):
    for x in rolelist:
        return int(x.times)


# 获取角色篇幅跨度
def get_span(*rolelist):
    for x in rolelist:
        return int(x.span)


# 存入篇幅跨度和出现次数
def save_something(name):
    role = Roles()
    role.name = name
    role.times = 0
    while True:
        role.sex = input("请输入该角色性别:")
        break
    while True:
        role.nick = input("请输入该角色的别名:")
        b = range(1, 121)
        for i in b:
            f = open('./data/chapter-{}.txt'.format(i), encoding='utf-8', errors='ignore')
            contents = f.read()
            if role.name in contents or role.nick in contents:
                role.times += 1
        for j in b:
            f = open('./data/chapter-{}.txt'.format(j), encoding='utf-8', errors='ignore')
            contents = f.read()
            if role.name in contents or role.nick in contents:
                break
        for k in reversed(b):
            f = open('./data/chapter-{}.txt'.format(k), encoding='utf-8', errors='ignore')
            contents = f.read()
            if role.name in contents or role.nick in contents:
                break
        role.span = k - j
        break
    while True:
        role.inf = input("请输入该角色的基本信息:")
        break
    Add(rolelist, role)


# 显示函数
def display(rolelist):
    print("{0:{6}^6}{1:{6}^10}{2:{6}^11}{3:{6}^25}{4:{6}^12}{5:{6}^10}".format("姓名", "性别", "别名", "基本信息", "出现次数", "篇幅跨度",
                                                                               chr(12288)))
    for item in rolelist:
        if item.nick == 'None':
            print("{0:{6}^6}{1:{6}^10}{2:{6}^12}{3:{6}^26}{4:{6}^13}{5:{6}^12}".format(item.name, item.sex, item.nick,
                                                                                       item.inf, item.times, item.span,
                                                                                       chr(12288)))
        else:
            print("{0:{6}^6}{1:{6}^10}{2:{6}^10}{3:{6}^25}{4:{6}^14}{5:{6}^11}".format(item.name, item.sex, item.nick,
                                                                                       item.inf, item.times, item.span,
                                                                                       chr(12288)))


# 初始化角色
def init(rolelist):
    print('初始化')
    file_object = open('roles.txt', 'r')
    for line in file_object:
        role = Roles()
        line = line.strip('\n')
        s = line.split(' ')
        role.name = s[0]
        role.sex = s[1]
        role.nick = s[2]
        role.inf = s[3]
        role.times = s[4]
        role.span = s[5]
        rolelist.append(role)
    file_object.close()
    print('初始化成功')
    main()


# 主函数
def main():
    while True:
        print("******************************")
        print('增加角色信息---1')
        print('查找角色信息---2')
        print('删除角色信息---3')
        print('修改角色信息---4')
        print('展示角色信息---5')
        print('按照出现次数排序---6')
        print('按照篇幅跨度排序---7')
        print('亲密度查询---8')
        print('退出程序---0')
        print("******************************")

        nchoose = input("请选择：")
        if nchoose == '1':
            role = Roles()
            role.name = input("输入角色姓名:")
            while True:
                if searchbyname(rolelist, role.name) == True:
                    print('该角色已存在')
                    role.name = input("请再次输入角色姓名:")
                else:
                    break

            save_something(role.name)


        if nchoose == '2':
            choose = input('''姓名查找---1
别名查找---2
请选择通过姓名查找还是别名查找:''')
            if choose == '1':
                name = input('请输入角色姓名:')
                search1(rolelist, name)
            if choose == '2':
                nick = input('请输入角色别名:')
                search2(rolelist, nick)

        if nchoose == '3':
            name = input("请输入要删除的角色:")
            Del(rolelist, name)

        if nchoose == '4':
            name = input("请输入要修改的角色:")
            change(rolelist, name)

        if nchoose == '5':
            display(rolelist)

        if nchoose == '6':
            a = input('''从高到低---1
从低到高---2
请选择:''')
            if a == '1':
                times_reduce(rolelist)
            if a == '2':
                times_rise(rolelist)

        if nchoose == '7':
            b = input('''从高到低---1
从低到高---2
请选择:''')
            if b == '1':
                span_reduce(rolelist)
            if b == '2':
                span_rise(rolelist)
        if nchoose == '8':
            qinmi(rolelist)

        if nchoose == '0':
            break


if __name__ == '__main__':
    rolelist = []
init(rolelist)