# i=0
# c=0
# while 1==1:
#     c=c+1
#     print('第'+str(c)+'天')
#     i=i+3
#     print("蜗牛在白天爬了3米,现在位于"+str(i)+"米处")
#     if i<7:
#         i=i-2
#         print('蜗牛在晚上下滑了2米,现在位于'+str(i)+"米处")
#         continue
#     else:
#         print('经过'+str(c)+"天可以爬出洞")
#         break

# i=0#乙
# j=i+18#甲
# while 1==1:
#     if (i-9)*2==j+9:
#         print('甲有'+str(j)+'只羊,乙有'+str(i)+'只羊')
#         break
#     else:
#         i=i+1
#         j=j+1


# a=input('请输入任意正整数:')
# l=[]
# for i in range(0,len(a)):
#     l.append(a[i])#字符串也可用索引!
# l.reverse()
# for i in range(0,len(l)):
#     print(l[i],end='')

# def sanjiao(a,b,c):
#     if a+b>c and b+c>a and c+a>b:
#         return 1
#     else:
#         return 0
#
# a=float(input('请输入a:'))
# b=float(input('请输入b:'))
# c=float(input('请输入c:'))
# d=sanjiao(a,b,c)
# print(d)

# a=int(input('请输入一个大于1的正整数:'))
# print('a可拆分为以下质因数:')
#
# l=[]
# for i in range(2,a+1):
#     l.append(i)
#
# for i in range(2, a + 1):
#     for j in range(2,a+1):
#         if i%j==0 and i!=j:
#             l.remove(i)
#             break
# def chengfang(a,b):#a的b次方
#     t=1
#     for i in range(b):
#         t=t*a
#     return t
#
# for i in l:
#     for j in range(1,a+1):
#         k1=chengfang(i,j)
#         k2=chengfang(i,j+1)
#         if a%k1==0 and a%k2!=0:
#             print(str(j)+'个'+str(i))
#             break



# a=int(input('请输入一个大于1的正整数:'))
# print(str(a)+'可拆分为以下质因数:')
#
# l=[]
# for i in range(2,a+1):
#     if a % i != 0:
#         continue
#     l.append(i)
#
# for i in l:
#     for j in range(2,a+1):
#         if i%j==0 and i!=j:
#             l.remove(i)
#             break
# print(l)#这个地方是用于测试bug的,这个程序最终给我拆成了下图中中括号的质因数,不知道为什么会拆成这样(我猜想应该是上面的程序默认会跳过一些数)
# def chengfang(a,b):#a的b次方
#     t=1
#     for i in range(b):
#         t=t*a
#     return t
#
# for i in l:
#     for j in range(1,a+1):
#         k1=chengfang(i,j)
#         k2=chengfang(i,j+1)
#         if a%k1==0 and a%k2!=0:
#             print(str(j)+'个'+str(i))
#             break


a=int(input('请输入一个大于1的正整数:'))
print(str(a)+'可拆分为以下质因数相乘:')

l=[]
for i in range(2,a+1):
    if a % i != 0:
        continue
    l.append(i)

c=[]
for i in l:
    for j in range(2,int((i+1)/2)):#这里整数的边界为此,因为i/2到i的数均与i互质
        if i%j==0 and i!=j:
            c.append(i)
            break
for i in c:
    l.remove(i)
print(l)

def chengfang(a,b):#a的b次方
    t=1
    for i in range(b):
        t=t*a
    return t

for i in l:
    for j in range(1,a+1):
        k1=chengfang(i,j)
        k2=chengfang(i,j+1)
        if a%k1==0 and a%k2!=0:
            print(str(j)+'个'+str(i))
            break