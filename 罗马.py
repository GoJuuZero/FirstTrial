def main():
    roma={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roma_input=input('请输入一个罗马数字:')
    a=0
    l=[]
    for i in roma_input:
        l.append(roma.get(i))
        if len(l)==1 or roma.get(i)<=b:
            a=a+roma.get(i)
        elif roma.get(i)>b:
            a=a-2*b+roma.get(i)
        b=roma.get(i)
    print(a)
if __name__ == '__main__':
    main()