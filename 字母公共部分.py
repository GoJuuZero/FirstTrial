import json
def main():
    l=input('请输入一个英文单词的列表,每个单词必须有双引号')
    l1=json.loads(l)
    b=len(l1[0])
    for i in l1:
        if len(i)<b:
            b=len(i)
    for i in range(len(l1)):
        exec('t{}=l1[{}]'.format(i,i))#创建动态变量
    l=[]
    for i in range(b):
        s = set()
        for j in range(len(l1)):
            exec('s.add(t{}[{}])'.format(j,i))
        if len(s)==1:
            l.append(list(s)[0])
            continue
        else:
            break
    print(l)
if __name__ == '__main__':
    main()