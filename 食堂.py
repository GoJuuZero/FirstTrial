i=0
l1=['糖醋排骨','干锅','宫保鸡丁','鱼香肉丝','鱼香茄子','番茄炒蛋','时令蔬菜']
l2=["001","002","003","004","005","006","007"]
l3=[22,26,22,20,16,12,10]

m=int(input('请输入你的现有金额:(输入0以退出程序,如果乱输的话会导致系统崩溃)'))
if m!=0:
    while 1 == 1:
        b=input('执行操作:(1.充值 2.消费 3.退出操作)')
        if b=='2':
            f=0
            while 1==1:
                    c = input('请输入菜品编号:(001,002,003,004,005,006,007)')
                    if c in l2:
                        if c=="001":
                            print('你选择了'+l1[0])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d>0:
                                e=d*l3[0]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        if c=="002":
                            print('你选择了'+l1[1])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d > 0:
                                e = d * l3[1]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        if c=="003":
                            print('你选择了'+l1[2])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d > 0:
                                e = d * l3[2]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        if c=="004":
                            print('你选择了'+l1[3])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d > 0:
                                e = d * l3[3]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        if c=="005":
                            print('你选择了'+l1[4])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d > 0:
                                e = d * l3[4]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        if c=="006":
                            print('你选择了'+l1[5])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d > 0:
                                e = d * l3[5]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        if c=="007":
                            print('你选择了'+l1[6])
                            d=int(input('请选择份数:(如果乱输的话会导致系统崩溃)'))
                            if d > 0:
                                e = d * l3[6]
                            else:
                                print('无效数值!请重选菜品!')
                                continue
                        f += e
                        k=input('还要选吗?(输入y可继续选,输入其他可结束选择)')
                        if k=='y':
                            continue
                        else:
                            pass
                        print('需花费'+str(f)+'元')
                        if m>f:
                            m-=f
                            print('成功付费,本次消费'+str(f)+'元,还剩'+str(m)+'元')
                        else:
                            print('余额不够,请充值!')
                        break
                    else:
                        print('请重新输入!')
                        continue
        elif b=='1':
            while 1==1:
                n=int(input('请输入充值金额:(如果乱输的话会导致系统崩溃)'))
                if n>0:
                    m+=n
                    print('充值成功!余额为'+str(m)+'元')
                    break
                else:
                    print('充值无效,请重新输入')
        elif b=='3':
            print('正在退出……')
            break
else:
    pass