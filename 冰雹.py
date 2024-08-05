while 1==1:
    i=input('请输入初始值:(输入0退出程序)')
    try:
        i=int(float(i))
    except ValueError:
        print('输入错误!')
        continue
    j=0
    if i>0:
        print(i,end=',')
        while i!=1:
            if i%2==0:
                i=i//2
            else:
                i=3*i+1
            j=j+1
            print(i,end=",")
        print('')
        print('一共经过了'+str(j)+'次变换')
    elif i==0:
        break
    else:
        print('输入错误!')
        continue
