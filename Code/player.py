#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A class Player"""

import dice


class Player():
    "Player Class"

    the_scores = []
    name = ''
    dic = {}

    def __init__(self):
        self.the_scores = []
        
    
    def scores(self):
        "Take all scores and put them into a list"
        die = dice.Dice()
        self.the_scores = []
        for x in range(0, 5):
            value = die.roll()
            self.the_scores.append(value)
        
        return self.the_scores
    
    def highScore(self, list_of_scores):
        "Taking a list of scores as a parameter and return the highest score"
        highest_number = 0
        
        for x in range(len(list_of_scores)):
            if highest_number < list_of_scores[x]:
               highest_number = list_of_scores[x]
        
        return highest_number

    def register_results(self, scores1):

        if self.name in self.dic.keys():
            self.dic[self.name].append(scores1)
        else:
            self.dic[self.name] = []
            self.dic[self.name].append(scores1)
        
        return self.dic[self.name]

    def get_the_game_resluts(self):
        return self.dic
    
    def show_player_results(self, player_score):
        for i in player_score:
            print(i)
    
    def change_the_name(self, new_name):

        self.dic[new_name] = self.dic.pop(self.name)
        dic1=self.dic  
        return dic1





if __name__ == '__main__':
    f = Player()
    s = f.scores()
    print(s)
    #print(f.register_results(s))
    #k = f.scores()
    #print(k)
    #print(f.register_results(k))
    #d = f.scores()
    #print(d)
    #print(f.register_results(d))
    #print(f.change_the_name('sss'))

