#生成随机数
#玩家生成数值
#判断输入数字大小
#输入正确答案，游戏结束
# import random
# answer=random.randint(1,100)
# gamer_num=int(input("please input number (1-100):"))
# while gamer_num!=answer:
#     if gamer_num>answer:
#         gamer_num = int(input("num is more please input number (1-100):"))
#     elif gamer_num<answer:
#         gamer_num = int(input("num is less please input number (1-100):"))
# print("you win the game")

import random

#生成随机数
ran_num=random.randint(1,100)
#玩家生成随机数值
game_num=int(input("please input your number(1-100:"))
#判断玩家数值是否匹配生成随机数
while game_num!=ran_num:
    if game_num>ran_num:
        game_num=int(input("num is bigger than ran_num please input another!!"))
    elif game_num<ran_num:
        game_num=int(input("num is less than ran_num please input another!!"))
print("you win the game!!")
