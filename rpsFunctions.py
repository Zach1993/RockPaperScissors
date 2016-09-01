import math
import decimal
import time
import datetime
import random
import re
import array
import scipy



def getUserAction():
    while True:
        player_input = input("Please choose either: Rock(r), Paper(p), or Scissors(s)?\n")
        if player_input not in frozenset(['s','r','p']):
            print("Input not valid, Please check your input and try again")
            continue
        else:
            break
    if player_input == "r":
        player_input_print = "Rock"
    elif player_input == "p":
        player_input_print = "Paper"
    elif player_input == "s":
        player_input_print = "Scissors"
    return player_input, player_input_print


def userActionRecord(p_user_action, r_count, p_count, s_count):
    user_action = p_user_action
    if user_action == "r":
        r_count += 1
    elif user_action == "p":
        p_count += 1
    elif user_action == "s":
        s_count += 1
    return r_count, p_count, s_count


def computerNextMove(r,p,s):
    sum_total = float(r + p + s)
    r_percent = float(r/sum_total)
    p_percent = float(p/sum_total)
    s_percent = float(s/sum_total)

    s_per_num = s_percent
    p_per_num = p_percent
    r_per_num = r_percent

    return r_per_num, p_per_num, s_percent, sum_total


def winLoss(comp, user, comp_count, user_count, draw_count):

    if comp == user:
        draw_count += 1
        return comp_count, user_count, draw_count
    elif (comp == "p" and user == "r") or (comp == "r" and user == "s") or (comp == "s" and user == "p"):
        comp_count += 1
        return comp_count, user_count, draw_count
    else:
        user_count += 1
        return comp_count, user_count, draw_count


def userPatternRecognition():
    # possible patterns by 3's
    # rrr rrp rpr rpp rrs rsr rss rsp rps
    # ppp ppr prp prr pps psp pss prs psr
    # sss ssr srs srr ssp sps spp srp spr
    pattern_list = ['','','']
    rrr
    rrp
    rpr
    rpp
    rrs
    rsr
    rss
    rsp
    rps
    ppp
    ppr
    prp
    prr
    pps
    psp
    pss
    prs
    psr
    sss
    ssr
    srs
    srr
    ssp
    sps
    spp
    srp
    spr

