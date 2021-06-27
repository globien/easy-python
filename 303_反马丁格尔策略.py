# -*-coding:utf-8 -*-

"""
# File       : 303_反马丁格尔策略.py
# Time       ：2020/8/10 下午3:01
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""

import random
import sys


class AntiMartingaleBet:
    def __init__(self, init_money, init_bet, wins_to_stop):
        self.money = self.init_money = init_money
        self.bet = self.init_bet = init_bet
        self.stop = wins_to_stop

    def one_bet(self):
        if random.randint(0, 1) == 1:
            self.money += self.bet
            self.bet *= 2                   # 如果赢了，赌注翻倍
            return 1
        else:
            self.money -= self.bet
            self.bet = self.init_bet        # 如果输了，重置赌注
            return 0

    def one_game(self, bet_times):
        wins_in_a_row = 0                   # 计数器，记录已经连赢多少次
        for i in range(bet_times):
            result = self.one_bet()
            wins_in_a_row += result
            wins_in_a_row *= result
            if wins_in_a_row == self.stop:  # 达到连赢目标次数，重置
                self.bet = self.init_bet
                wins_in_a_row = 0
        game_earning = self.money - self.init_money
        return game_earning


trial = 8000
total_earning = 0
for i in range(trial):
    myBet = AntiMartingaleBet(init_money=63, init_bet=1, wins_to_stop=4)
    earning = myBet.one_game(bet_times=200)
    total_earning += earning
    print('第{:4d}盘盈利: {:4d}'.format(i+1, earning))

print('平均每盘盈利: {}'.format(total_earning/trial))
