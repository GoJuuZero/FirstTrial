import json
def read():
    with open(r'C:\Users\Administrator\Desktop\Test\高考.txt','r') as file:
        f=file.read()
    f=json.loads(f)
    return f

def write1():
    nameinput = input('请输入考生姓名')
    scoreinput = float(input('请输入考生分数'))
    f=[]
    inf = {nameinput: scoreinput}
    try:
        f=read()
    except FileNotFoundError:
        pass
    f.append(inf)
    f=json.dumps(f,ensure_ascii=False)
    with open(r'C:\Users\Administrator\Desktop\Test\高考.txt', 'w') as file:
        file.write(f)
    print('写入成功!')

def delete():
    nameinput = input('请输入考生姓名')
    try:
        f = read()
    except FileNotFoundError:
        pass
    k=0
    for i in f:
        if [nameinput]==list(i):
            f.remove(i)
            k=1
    if k==1:
        f=json.dumps(f,ensure_ascii=False)
        with open(r'C:\Users\Administrator\Desktop\Test\高考.txt', 'w') as file:
            file.write(f)
        print('移除成功!')
    elif k==0:
        print('没有此人!')


def main():
    while True:
        choice=input('请输入你的操作:1,加入考生数据 2.读取考生数据 3.删除考生数据 4.退出')
        if choice=='1':
            write1()
        elif choice=='2':
            f=read()
            print(f)
        elif choice=='3':
            delete()
        elif choice=='4':
            break
        else:
            print('Error')





if __name__ == '__main__':
    main()