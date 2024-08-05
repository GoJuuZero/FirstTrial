import random
import time

def main():
    # lista=[1,3,2]
    # lista.sort()
    # i=0
    # while True:
    #     listb=[]
    #     while True:
    #         k=random.choice(lista)
    #         if not k in listb:
    #             listb.append(k)
    #         print(listb)
    #         time.sleep(0.5)
    #         #以上两排为debug
    #         if len(listb)==len(lista):
    #             break
    #     i+=1
    #     print('----这是第'+str(i)+'次运行----')
    #     if listb==lista:
    #         print('排序结束!共运行了'+str(i)+'次')
    #         break


    lista=[1,3,2]
    lista.sort()
    i=0
    while True:
        listb=[]
        while True:
            k=random.choice(lista)
            if not k in listb:
                listb.append(k)
            print(listb)
            time.sleep(0.5)
            #以上两排为debug
            if len(listb)==len(lista):
                break
        i+=1
        print('----这是第'+str(i)+'次运行----')
        if listb==lista:
            print('排序结束!共运行了'+str(i)+'次')
            break
if __name__ == '__main__':
    main()