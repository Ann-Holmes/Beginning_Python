import sys, shelve


def store_person(db):
    """
    让用户输入数据并将其存储到shelf对象中
    :param db: dict
    :return: None
    """
    pid = input("Enter unique ID number: ")
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person

def lookup_person(db):
    """
    让用户输入ID和所需的字段, 并从shelf对象中获取相应的数据
    :param db:dict
    :return:None
    """
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone)')
    field = field.strip().lower() # 格式化输入

    print(field.capitalize() + ':', db[pid][field])

def print_help():
    """
    打印到相关命令的帮助信息到屏幕上
    :return: None
    """
    print("The availabel commands are: ")
    print('store  : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit   : Save changes and exit')
    print('?      : Prints this message')

def enter_command():
    """
    标准化用户输入的命令
    :return: str
    """
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    """
    主函数
    :return: None
    """
    database = shelve.open('/home/andy/Documents/Learning/Beginning_Python/10_module/10.3/database.dat')  # 设置数据库存储路径
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                sys.exit()
    finally:
        database.close()


if __name__ == '__main__': main()
