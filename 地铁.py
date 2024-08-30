#这个是由b站的一个视频而解析出的程序,在这里声明感谢up主如歌的小日子
import os,json,time
class map:
    def __init__(self):
        self.bata = map.document_Read(self,"地铁题库.json")

    def document_Read(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    def Output(self):
        num = 0
        for i in range(len(self.bata)):
            print(f"第{i + 1}题，请根据以下提示猜城市：")
            num+=map.Answer_the_questions(self,i)
            print("你的得分为"+str(num))
    def Answer_the_questions(self,i):
        for j in range(3):
            a = input(self.bata[str(i)][0]["题干"][str(j)] + "\n输入答案或回车揭开提示？")
            if a == self.bata[str(i)][0]["城市"]:
                print("您揭开了" + str(j + 1) + "个提示，获得了" + str(20 - ((j) * 5)) + "分")
                print(self.bata[str(i)][0]["解析"])
                return (20 - ((j) * 5))
            if j >= 2 and a != self.bata[str(i)][0]["城市"]:
                print("答题失败")
                return 0


    def main(self):
        print('--------欢迎您游玩轨交城市游戏--------')
        print('本游戏共5题,每题会有3个提示,第一次提示给出后,您可以抢答,也可以再揭开一条提示,依次到第三个提示被揭开后您必须作答')
        print('揭开第一个提示可得20分,第二个为15分,第三个为10分,答错0分')
        map.Output(self)
game = map()
game.main()