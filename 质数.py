# while 1==1:
#     a=input('请输入一个大于1的整数(输入0以退出程序):')
#     l=[]
#     try:
#         a=int(a)
#     except ValueError:
#         continue
#     for i in range(2,a+1):
#         l.append(i)
#     if a>1:
#         for i in range(2, a + 1):
#             for j in range(2,a+1):
#                 if i%j==0 and i!=j:
#                     l.remove(i)
#                     break
#         print('1到'+str(a)+'以内的质数有:',l,'共'+str(len(l))+'个质数')
#         continue
#     elif a==0:
#         print('正在退出程序……')
#         break
#     else:
#         continue
#
# #以下为质因数,我稍微简化了一下运算过程
# a=int(input('请输入一个大于1的正整数:'))
# print(str(a)+'可拆分为以下质因数:')
#
# l=[]
# for i in range(2,a+1):
#     if a % i != 0:
#         continue
#     l.append(i)
#
# c=[]
# for i in l:
#     for j in range(2,a+1):
#         if i%j==0 and i!=j:
#             c.append(i)
#             break
# for i in c:
#     l.remove(i)
#
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

# a=input('请输入一个整数:')
# l=[]
# for i in range(2,a+1):
#     l.append(i)
# if a>1:
#     for i in range(2, a + 1):
#         for j in range(2,a+1):
#             if i%j==0 and i!=j:
#                 l.remove(i)
#                 break
#     print('1到'+str(a)+'以内的质数有:',l,'共'+str(len(l))+'个质数')
#     continue
# elif a==0:
#     print('正在退出程序……')
#     break
# else:
#     continue