# -*- coding: utf-8 -*-
"""
Created on Thu Oct 4 21:22:05 2018

@author: Alan Jerry Pan, CPA, CSc
@affiliation: Shanghai Jiaotong University

Program used for experimental study of (i) game theory, (ii) behavioral psychology, and (iii.) memory.

Arguably the best test to evaluate whether a human is talking to a chicken or a machine.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Chicken Arena [Computer software]. Github repository <https://github.com/alanjpan/Chicken-Arena>

Note this software's license is GNU GPLv3.
"""

import random
import sys

turns = 0
bawkcounter = 0
secure_random = random.SystemRandom()
chickenAIs = ['cluck', 'cluck', 'cluck', 'bawk', 'peck', 'stare', 'stare', 'fly', 'sleep', 'egg']
say = ""

############################################################
def cluck():
    global say
    say = "CLUCK"
    
def bawk():
    global bawkcounter
    bawkcounter += 1
    
    global say
    say = "BAWK"
    
def peck():
    global say
    say = "*peck*"
    
def stare():
    global say
    say = "*stare*"
    
def fly():
    global say
    say = "*flap*"
    
def sleep():
    global say
    say = "zzz"
    
def egg():
    global say
    say = "*plop*"

def dinner():
    gameover()

############################################################

def chickenAI():
    action = secure_random.choice(chickenAIs)
    exec(compile(action + '()', '', 'exec'))
    print('\t\t' + say)

def CHICKEN():
    global bawkcounter
    global turns
    bawkcounter = 0
    turns = 0
    
    while bawkcounter < 3:
        print('O>..................<0')
        print('... ... ... ... ...')
        print('(cluck / bawk / ...?)')
        action = input().lower()
        try:
            exec(compile(action + '()', '', 'exec'))
            print(say)
        except Exception:
            print('?')
        turns += 1
        chickenAI()
    gameover()

def gameover():
    print('\n\n')
    print('... ' + str(turns) + ' turns...')
    print('Play again? (ye/no)')
    if input().lower().startswith('ye'):
        main()
    else:
        sys.exit()

def main():
    print('\n\nCHICKEN ARENA\n')
    print('You, a chicken, are caught in an unfortunate situation with another chicken. Both of you chickens are trapped and only one may leave the arena. Both chickens end up dinner. There is no victory.')
    print('Yes / No')
    if input().lower().startswith('ye'):
        CHICKEN()
    else:
        gameover()

main()