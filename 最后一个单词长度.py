def main():
    s=input('请输入一句英文,单词与单词之间不要使用标点符号,用空格隔开')
    l=[]
    for i in range(len(s)-1,-1,-1):
        if s[i]==' ':
            break
        else:
            l.append(s[i])
    print(len(l))
if __name__ == '__main__':
    main()