def main():
    a=input('请输入一个整数:')
    l1=[]
    l2=[]
    for i in range(len(a)):
        l1.append(a[i])
    for j in range(len(a)-1,-1,-1):
        l2.append(a[j])
    if l1==l2:
        print('为回文数')
    else:
        print('不为回文数')

if __name__ == '__main__':
    main()